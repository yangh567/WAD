from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView

from PostBar.meta_views import IUpdateView, IDetailView, IListView, ICreateView
from PostBar.forms import UserForm, UserProfileForm
from PostBar.models import UserProfile, Category, Question, Answer
from PostBar.util import to_int


def index(request):
    context_dict = {'boldmessage': "How's the day"}
    return render(request, 'PostBar/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': "Zhouyang shen    ,   Yixuan Dai   ,   Ming Ho Wu"}
    return render(request, 'PostBar/about.html', context=context_dict)


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.

            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
        # Render the template depending on the context.
    return render(request,
                  'PostBar/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'PostBar/login.html', {})


def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


def user_profile_detail(request, user_id: int):
    """view the user profile"""
    return render(request,
                  'PostBar/user_profile_detail.html',
                  {'profile_form': get_object_or_404(UserProfile, user_id=user_id)})


@login_required
def edit_user_profile(request):
    """edit the user profile or start an edition of user profile
    if the edition is success redirect back to the users own detail page
    """
    user = request.user
    # edition if it is a post and one can only edit profile of itself
    if request.method == 'POST':
        # Get the form from update data and login user
        profile_form = UserProfileForm(data=request.POST, instance=user.userprofile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return redirect("user_profile_detail", user.id)
        else:
            print(profile_form.errors)
    else:
        # generate user profile from user
        profile_form = UserProfileForm(instance=user.user_profile)
    return render(request,
                  'PostBar/edit_user_profile.html',
                  {'profile_form': profile_form})


# @login_required
def user_profile_list(request, page):
    """page the user_profile_list and return """
    query_name = request.GET.get('query_name')
    query_location = request.GET.get('query_location')
    user_profiles = UserProfile.objects.filter(user__username__iexact=query_name, location__iexact=query_location).all()
    profiles = page_list(user_profiles, page)
    return render(request,
                  'PostBar/user_profile_list.html',
                  {'profile_form': profiles})


def following_list(request, user_id, page):
    """page the flowing list and return """
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    followers = page_list(user_profile.followings.all(), page)
    return render(request,
                  'PostBar/following_list.html',
                  {"followers": followers})


def follower_list(request, user_id, page):
    """page the follower list and return follower paginator"""
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    followers = page_list(user_profile.followers.all(), page)
    return render(request,
                  'PostBar/following_list.html',
                  {"followers": followers})


def page_list(object_list, page, max_page_number=25):
    """take an object list and page it
    return a paginator
    """
    paginator = Paginator(object_list, max_page_number)
    if paginator.num_pages < page: page = 1
    followers = paginator.page(page)
    return followers


@login_required
def add_following(request):
    """if id is right add to following then redirect"""
    user = request.user
    if request.method == 'POST':
        follow_id = request.POST.get('follow_id')
        user.userprofile.add_following(follow_id)
        redirect("following_list", user.id, 1)


@login_required
def delete_following(request):
    """if id is right delete the following then redirect"""
    user = request.user
    if request.method == 'POST':
        follow_id = request.POST.get('follow_id')
        user.userprofile.delete_following(follow_id)
        redirect("following_list", user.id, 1)


### Category
class CategoryCreateView(ICreateView):
    model = Category
    fields = ['name']


class CategoryUpdateView(IUpdateView):
    model = Category
    fields = ['name']


class CategoryDetailView(IDetailView):
    model = Category
    fields = ['name']


class CategoryListView(ListView):
    model = Category
    context_object_name = "category_list"
    paginate_by = 5


### Question
class QuestionCreateView(ICreateView):
    model = Question
    fields = ['title', 'content', 'category']

    def get_form(self, form_class=None):
        """fetch in a user to the form if it is a post"""
        if self.request.method == 'POST':
            form = super().get_form(form_class)
            m = form.save(commit=False)
            m.user = self.request.user
            return form


class QuestionUpdateView(IUpdateView):
    model = Question
    fields = ['title', 'content']

    def get_object(self, *args, **kwargs):
        obj: Question = super().get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj


class QuestionDetailView(IDetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        object: Question = self.get_object()
        object.add_views()

        page = to_int(self.request.GET.get('page'))
        page_obj = page_list(object.answers.all(), page, 5)
        context["is_paginated"] = True
        context['page_obj'] = page_obj
        context['answer_list'] = page_obj.object_list
        return context


class QuestionListView(IListView):
    model = Question
    context_object_name = "question_list"
    paginate_by = 3
    ordering = 'last_modified'
    filter_keys = ['category_id']

    def get_queryset(self):
        """ search for question title
        """
        new_context = super().get_queryset()
        new_context = new_context.filter(**self.get_filter_kwargs())
        query = self.request.GET.get("query")
        if query:
            new_context = new_context.filter(title__contains=query)
        # new_context = new_context.annotate(num_submissions=Count('answers')).order_by('-answers')
        return new_context

    def get_context_data(self, **kwargs):
        """add query keys back to context so you can get it from template"""
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query")
        if query:
            context["query"] = query
        return context


### Answer
class AnswerListView(IListView):
    model = Answer
    context_object_name = "answers_list"
    paginate_by = 5
    ordering = 'last_modified'
    filter_keys = ['question_id']


class AnswerCreateView(ICreateView):
    model = Answer
    fields = ['content']

    def get_form(self, form_class=None):
        """get the form and attach users"""
        try:
            question_id = self.kwargs['question_id']
            question = Question.objects.get(id=question_id)
        except:
            raise Http404
        else:
            form = super().get_form(form_class)
            m: Answer = form.save(commit=False)
            m.user = self.request.user
            m.question = question
            return form


class AnswerDetailView(IDetailView):
    model = Answer


class AnswerUpdateView(IUpdateView):
    model = Answer
    fields = ['content']

    def get_object(self, *args, **kwargs):
        obj: Answer = super().get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj
