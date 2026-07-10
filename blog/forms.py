from django import forms
from django.core.exceptions import ValidationError

from .models import Blog


class BlogFormView(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "content",
            "image",
        )

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or title.strip() == "":
            raise ValidationError("Название блога не может быть пустым!")
        return title
