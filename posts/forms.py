from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Post
from users.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "avatar", "description"]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "description", "status"]