from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class ProfileUpdateForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass  # pakai default bawaan Django
