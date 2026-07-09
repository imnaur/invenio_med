from django.test import TestCase
from django.urls import reverse
from blog.models import Blog


class HomeTemplateTest(TestCase):
    def setUp(self):
        for i in range(5):
            Blog.objects.create(title=f"Post {i}", content="Content")

    def test_homepage_loads_correctly(self):
        """Проверяем, что главная открывается и показывает посты"""
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["blogs"]), 3)
