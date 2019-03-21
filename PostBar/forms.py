from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from PostBar.models import UserProfile


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
            raise forms.ValidationError("username has been used")
        return val

    def clean_email(self):
        val = self.cleaned_data['email']
        if not val:
            raise forms.ValidationError("You need to fill in the email field")
        elif User.objects.exclude(pk=self.instance.pk).filter(email__exact=val):
            raise forms.ValidationError("email has been used")
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
