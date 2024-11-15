from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2",)


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()


class UserResetPasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ['email', ]
