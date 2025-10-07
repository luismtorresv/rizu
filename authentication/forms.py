from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


class OpenStackUserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            ("project_manager", "Project Manager"),
            ("user", "User"),
        ]
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "role")
