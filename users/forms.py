from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "email")

class SignupChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")