from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=False, min_value=1, help_text="Optional. Enter your age.")

    class Meta:
        model = CustomUser
        fields = ("email", "username", "age", "first_name", "last_name", "phone", "is_active", "password1", "password2")