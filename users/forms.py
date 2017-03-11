# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from models import Profile


class LoginForm(forms.Form):
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        """fields = (
            'username',
            'password',
            'email'
        )"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'usuario',
            'phone',
            'centro',
            'responsable'
        )
