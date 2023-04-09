from django import forms
from django.contrib.auth.forms import UserCreationForm, User



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        }
    ))


class SignForm(UserCreationForm, forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
    attrs={
    'class': 'form-control',
    'placeholder': "First Name",
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder': "Last Name",
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs = {
        'class':'form-control',
        'placeholder': 'Your Email',
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder': "Username",
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder': "Password",
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder': "Re-Type-Password",
        }
    ))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']