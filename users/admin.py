from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "is_patient",
        "is_doctor",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "date_of_birth",
        "address",
    )
    list_display_links = ("email",)
