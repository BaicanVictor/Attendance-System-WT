from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'style': "width:100%;"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'style': "width:100%;"}))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(required=True, label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(required=True, label="Password confirmation",
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))


    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]
