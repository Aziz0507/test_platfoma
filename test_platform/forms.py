from dataclasses import field
from django import forms
from .models import Test_question

class Test_quest_form(forms.ModelForm):
    class Meta:
        model = Test_question
        # fields = ['options_A', 'options_B', options_C]