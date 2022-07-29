from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username','password']