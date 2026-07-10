from django.urls import path

from catalog.views import (
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailView,
    ServiceListView,
    ServiceUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="service_list"),
    path("service/create/", ServiceCreateView.as_view(), name="service_create"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path(
        "service/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"
    ),
    path(
        "service/<int:pk>/update/", ServiceUpdateView.as_view(), name="service_update"
    ),
]
