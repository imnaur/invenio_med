from modeltranslation.translator import TranslationOptions, register

from .models import StaticPage


@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content",
    )
