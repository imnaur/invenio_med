from django.db import models


class StaticPage(models.Model):
    title = models.CharField(
        max_length=55,
    )
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="pages_content/", blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    slug = models.SlugField(max_length=55, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Письмо {self.message} от отправителя {self.email}"

    class Meta:
        verbose_name = "Сообщение пациентов"
        verbose_name_plural = "Сообщения пациентов"
