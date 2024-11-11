import secrets
import string
from random import random

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, UserResetPasswordForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message="f'Перейти по ссылке для подтверждения почты {url}'",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserResetPasswordView(FormView):
    model = User
    form_class = UserResetPasswordForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            if user:
                password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                user.set_password(password)
                user.is_active = True
                user.save()
                send_mail(
                    subject="Сброс пароля",
                    message=f'Новый пароль: {password}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
            return redirect(reverse("users:login"))
        except User.DoesNotExist:
            return redirect(reverse("users:register"))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
