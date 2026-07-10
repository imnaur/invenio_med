from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testdoctor", email="doctor@example.com", password="password123"
        )

    def test_user_creation(self):
        """Проверяем, что пользователь создан и данные верны"""
        self.assertEqual(self.user.username, "testdoctor")
        self.assertEqual(self.user.email, "doctor@example.com")
        self.assertTrue(self.user.check_password("password123"))
        self.assertTrue(self.user.is_active is True)

    def test_str_method(self):
        """Проверяем метод __str__"""
        self.assertEqual(str(self.user), "doctor@example.com")
