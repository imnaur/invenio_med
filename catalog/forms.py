from django import forms
from .models import Service
from django.core.exceptions import ValidationError


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Service
        fields = (
            "name",
            "description",
            "price",
            "duration",
            "service_type",
            "completion_date",
            "rules",
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена услуги не может быть отрицательной!")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name or name.strip() == "":
            raise ValidationError("Название услуги не может быть пустым!")
        return name
