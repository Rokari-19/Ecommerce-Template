from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2' )
       
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':' py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class':' py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':' py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Retype Password',
        'class':' py-4 px-6 rounded-xl'
    }))




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':' py-4 px-6 rounded-xl'
    }), required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':' py-4 px-6 rounded-xl'
    }), required=True)
