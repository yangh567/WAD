from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from PostBar.models import UserProfile, Question, Category


def index(request):
    context_dict = {'boldmessage': "How's the day"}
    return render(request, 'PostBar/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': "Zhouyang shen    ,   Yixuan Dai   ,   Ming Ho Wu"}
    return render(request, 'PostBar/about.html', context=context_dict)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'email', 'password')

    def clean_username(self):
        val = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username__exact=val):
            raise forms.ValidationError("username is duplicated")
        return val

    def clean_email(self):
        val = self.cleaned_data['email']
        if not val:
            raise forms.ValidationError("email is required")
        elif User.objects.exclude(pk=self.instance.pk).filter(email__exact=val):
            raise forms.ValidationError("email is duplicated")
        else:
            return val


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'location', 'background')


class UserProfileUpdateForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'location', 'background')

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ("id")
#
#
#
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('title', 'content', 'category')
#         private_fields= []
