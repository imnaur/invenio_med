from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=115, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=115, verbose_name=_("Фамилия"))
    email = models.EmailField(unique=True, verbose_name=_("Адрес почты"), max_length=55)
    phone_number = models.CharField(
        max_length=20, verbose_name=_("Номер телефона"), blank=True, null=True
    )
    date_of_birth = models.DateField(
        verbose_name=_("Дата рождения"), blank=True, null=True
    )
    address = models.CharField(
        max_length=255, verbose_name=_("Адрес пациента"), blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email
