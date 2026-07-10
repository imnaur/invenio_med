from modeltranslation.translator import TranslationOptions, register

from .models import Blog


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content",
    )
