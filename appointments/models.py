from django.db import models
from catalog.models import Service
import uuid

from users.models import CustomUser
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES_APPOINTMENT = [
    ("created", _("Создана")),
    ("confirmed", _("Подтверждена")),
    ("completed", _("Завершена")),
]

STATUS_CHOICES_RESULT = [
    ("in progress", _("В работе")),
    ("ready", _("Готово")),
]


class Appointment(models.Model):
    patient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("Пациент")
    )
    date = models.DateTimeField(verbose_name=_("Дата и время записи"))
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name=_("Услуга")
    )
    status = models.CharField(
        default="created", verbose_name=_("Статус"), choices=STATUS_CHOICES_APPOINTMENT
    )
    barcode_id = models.UUIDField(default=None, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.service.service_type == "lab_test" and not self.barcode_id:
            self.barcode_id = uuid.uuid4()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.service} для {self.patient}"


class DiagnosticResult(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        verbose_name=_("Запись"),
        related_name="diagnostic_result",
    )
    result_text = models.TextField(max_length=255, verbose_name=_("Текст результата"))
    file = models.FileField(
        upload_to="m/",
        help_text=_("Загрузите PDF анализов"),
        verbose_name=_("PDF анализов"),
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата и время загрузки анализов")
    )
    status = models.CharField(
        verbose_name=_("Статус результата"), choices=STATUS_CHOICES_RESULT
    )

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"

    def __str__(self):
        return self.status
