from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import (CustomUserAuthenticationForm, CustomUserCreationForm,
                    CustomUserProfileForm)
from .models import CustomUser


class RegisterView(CreateView):
    """Класс для регистрации юзеров"""

    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("pages:home")

    def form_valid(self, form):
        """Метод отправляет WELCOME письмо на почту юзера"""
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Метод по отправке письма"""
        subject = "Добро пожаловать!"
        message = "Спасибо за регистрацию на нашем сайте клиники!"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )


class CustomLoginView(LoginView):
    """Класс для Log IN"""

    form_class = CustomUserAuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy("pages:home")

    def get_success_url(self):
        return reverse_lazy("pages:home")


class CustomUserProfileView(LoginRequiredMixin, DetailView):
    """Класс для профиля юзера"""

    model = CustomUser
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        """Метод возвращает определенного юзера"""
        return self.request.user


class CustomUserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для обновления профиля юзера"""

    model = CustomUser
    form_class = CustomUserProfileForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/profile_update.html"

    def get_object(self, queryset=None):
        """Метод возвращает определенного юзера"""
        return self.request.user
