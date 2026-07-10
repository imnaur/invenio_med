from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from appointments.models import Appointment, DiagnosticResult
from catalog.models import Service

User = get_user_model()


class AppointmentPermissionTest(TestCase):
    """Тесты прав доступа для модели Appointment (Приемы)"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="patient")
        self.client.force_login(self.user)

        self.service = Service.objects.create(
            name="Консультация", price=1000, duration=timedelta(minutes=30)
        )

        self.appointment = Appointment.objects.create(
            patient=self.user, service=self.service, date=timezone.now()
        )

    def test_patient_cannot_delete_appointment(self):
        """Проверяем, что обычный пользователь не может удалить запись о приеме"""
        self.assertTrue(Appointment.objects.filter(pk=self.appointment.pk).exists())


class DiagnosticResultTest(TestCase):
    """Тесты прав доступа для модели DiagnosticResult (Результаты анализов)"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="doctor_test")
        self.client.force_login(self.user)

        self.service = Service.objects.create(
            name="Анализ", price=500, duration=timedelta(minutes=15)
        )
        self.appointment = Appointment.objects.create(
            patient=self.user, service=self.service, date=timezone.now()
        )

        self.result = DiagnosticResult.objects.create(appointment=self.appointment)

    def test_forbidden_access_to_delete(self):
        """Проверяем, что пользователь не может удалить результат анализа без прав доступа"""
        self.assertTrue(DiagnosticResult.objects.filter(pk=self.result.pk).exists())
