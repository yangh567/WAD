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


class UserProfileForm(forms.ModelForm):
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
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content', 'category')
        private_fields= []
