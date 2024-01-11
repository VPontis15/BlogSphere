
from django.forms import ModelForm
from django import forms
from .models import Post




class PostForm(ModelForm):
   
    class Meta:
        model = Post
        fields = ("title", "body", "tags")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": " Enter blog's title"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "options"})
        }
        labels = {
            "tags": "available tags"
        }
        error_messages = {
            "tags": {"required":"Please select at least one tag"},
            "body": {"required":"The content of the blog cannot be empty!"}
        }


        
