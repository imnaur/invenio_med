from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Appointment, DiagnosticResult


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["date", "status", "service"]

    date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"},
            format="%Y-%m-%dT%H:%M",
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].required = False
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def clean_date(self):
        data = self.cleaned_data.get("date")
        if not data and not (self.instance and self.instance.date):
            raise forms.ValidationError(_("Дата обязательна для записи."))
        return data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data.get("date"):
            instance.date = self.instance.date
        if commit:
            instance.save()
        return instance


class DiagnosticResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = DiagnosticResult
        fields = (
            "appointment",
            "result_text",
            "file",
            "status",
        )
