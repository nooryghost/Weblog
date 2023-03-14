from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import SignupForm, SignupChangeForm

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = SignupForm
    form = SignupChangeForm
    model = User
    list_display = ("username", "email", "avatar", "is_staff")

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("avatar",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("avatar",)}),)