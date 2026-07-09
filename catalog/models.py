from django.db import models
from django.utils.translation import gettext_lazy as _

SERVICES = [
    ("lab_test", _("Лабораторный анализ")),
    ("doctor_appointment", _("Запись к врачу")),
]

LAB_RULES = [
    ("On an empty stomach", _("Натощак")),
    ("Don't eat for two hours", _("Не есть за два часа")),
    ("No rules", _("Нет ограничений")),
]


class Service(models.Model):
    name = models.CharField(max_length=55, verbose_name=_("Название услуги"))
    description = models.TextField(max_length=255, verbose_name=_("Описание услуги"))
    price = models.IntegerField(verbose_name=_("Цена услуги"))
    duration = models.DurationField(verbose_name=_("Продолжительность"))
    service_type = models.CharField(verbose_name=_("Тип услуги"), choices=SERVICES)
    completion_date = models.CharField(verbose_name=_("Срок выполнения"), max_length=55)
    rules = models.CharField(
        verbose_name=_("Правило подготовки для сдачи анализа"), choices=LAB_RULES
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
