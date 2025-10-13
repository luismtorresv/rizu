from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import OpenStackUser


class OpenStackUserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            ("project_manager", "Project Manager"),
            ("member", "User"),
        ]
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "role")
