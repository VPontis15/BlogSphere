from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class  UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



