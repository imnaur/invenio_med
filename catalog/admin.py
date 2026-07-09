from django.contrib import admin

from catalog.models import Service
from pages.models import ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "duration",
        "service_type",
        "completion_date",
        "rules",
    )
    search_fields = (
        "name",
        "service_type",
    )
    list_filter = ("service_type",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("email", "message", "created_at")
    search_fields = ("email",)
