from django.contrib import admin

from appointments.models import Appointment, DiagnosticResult


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "date", "service", "status", "barcode_id")
    search_fields = ("patient",)
    list_filter = ("service", "status")


@admin.register(DiagnosticResult)
class DiagnosticResultAdmin(admin.ModelAdmin):
    list_display = ("appointment", "result_text", "file", "uploaded_at", "status")
    search_fields = ("appointment",)
    list_filter = ("status",)
