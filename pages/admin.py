from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

import pages.translation
from pages.models import StaticPage


@admin.register(StaticPage)
class StaticPageAdmin(TranslationAdmin):
    list_display = ["title", "content", "image", "updated_at", "slug"]
    search_fields = ("title", "updated_at")
    list_filter = ("updated_at",)
