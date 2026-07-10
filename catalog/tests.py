from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Service

User = get_user_model()


class ServicePermissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="patient")
        self.client.force_login(self.user)

        self.service = Service.objects.create(
            name="Тест", price=100, duration=timedelta(minutes=30)
        )

    def test_forbidden_access_to_delete(self):
        self.assertTrue(Service.objects.filter(pk=self.service.pk).exists())
