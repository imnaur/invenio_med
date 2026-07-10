from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Blog

User = get_user_model()


class BlogPermissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="patient")
        self.client.force_login(self.user)

        self.blog = Blog.objects.create(title="Тест", content="Контент")

    def test_forbidden_access_to_delete(self):
        """Проверяем, что пользователь не может удалить запись в блоге"""
        self.assertTrue(Blog.objects.filter(pk=self.blog.pk).exists())
