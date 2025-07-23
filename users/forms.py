from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings

class ProfileUpdateForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass  # pakai default bawaan Django

class UserRegisterForm(UserCreationForm):
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
