from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include("pages.urls", namespace="pages")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("appointments/", include("appointments.urls", namespace="appointments")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("chatbot/", include("chatbot.urls", namespace="chatbot")),
    path("users/", include("users.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
