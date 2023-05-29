from django.contrib.auth import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length= 20)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2']