from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=55,
    )
    content = models.TextField(
        max_length=1255,
    )
    image = models.ImageField(upload_to="blog/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
