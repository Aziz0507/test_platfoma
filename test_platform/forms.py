from dataclasses import field, fields
from django import forms
from .models import Test_question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register_Form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
