from django.urls import path
from pages.views import HomeTemplateView, StaticPageView

app_name = "pages"

urlpatterns = [
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("<slug:page_slug>/", StaticPageView.as_view(), name="page_detail"),
]
