from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserChangeForm
from .models import Profile


class  UserForm(forms.ModelForm):
    email = forms.EmailField( required=False)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    class Meta:
        model = Profile
        exclude = ["following", "followers", 'user','comments']

    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        if self.instance:
                self.fields['email'].initial = self.instance.user.email
                self.fields['first_name'].initial = self.instance.user.first_name
                self.fields['last_name'].initial = self.instance.user.last_name


class ChangingPasswordForm(PasswordChangeForm):
     username = forms.CharField(required=False)
     old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'type': 'password'}))
     new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'type': 'password'}))
     new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'type': 'password'}))
    
     class Meta:
        model = User
        fields = ['username', 'old_password', 'new_password1', 'new_password2']




     
        