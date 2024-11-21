# This file is to include all of the fields from the model.py

from django import forms
from .models import*

class AddUserProfileForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'