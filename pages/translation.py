from modeltranslation.translator import register, TranslationOptions
from .models import StaticPage


@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content",
    )
