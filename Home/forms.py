# This file is to include all of the fields from the model.py

from django import forms
from .models import*
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_image', 'event_start', 'event_end', 'event_location', 'event_description', 'ticket_price', 'is_private', 'event_capacity']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'placeholder': 'Enter event name...',
                'class': 'event-name-input'
            }),
            'event_image ': forms.ImageField(widget=forms.FileInput(attrs={
                'id': 'upload-photo',
                'class': 'upload-photo-btn',
                'accept': 'image/*'
            })),
            'event_start': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'date-time-input'
            }),
            'event_end': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'date-time-input'
            }),
            'ticket_price': forms.NumberInput(attrs={
                'min': 0,
                'step': 0.01,
                'class': 'ticket-input'
            }),
            'event_description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'description-input',
                'placeholder': 'Enter event description...'
            }),
            'event_capacity': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': '0',
                'class': 'capacity-input' 
            }),
            'event_location': forms.TextInput(attrs={
                'placeholder': 'Enter On-site Address or Online Link',
                'class': 'location-input'
            }),
            'is_private': forms.CheckboxInput(attrs={
                'class': 'switch-input'
            })
        }