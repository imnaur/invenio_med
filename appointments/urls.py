from django.urls import path
from appointments.views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentUpdateView,
    DiagnosticResultListView,
    DiagnosticResultCreateView,
    DiagnosticResultUpdateView,
    DiagnosticResultDeleteView,
    DiagnosticResultDetailView,
)

app_name = "appointments"

urlpatterns = [
    path("list/", AppointmentListView.as_view(), name="appointment_list"),
    path("create/", AppointmentCreateView.as_view(), name="appointment_create"),
    path(
        "<int:pk>/detail/", AppointmentDetailView.as_view(), name="appointment_detail"
    ),
    path(
        "<int:pk>/delete/", AppointmentDeleteView.as_view(), name="appointment_delete"
    ),
    path(
        "<int:pk>/update/", AppointmentUpdateView.as_view(), name="appointment_update"
    ),
    path("result/list/", DiagnosticResultListView.as_view(), name="result_list"),
    path("result/create/", DiagnosticResultCreateView.as_view(), name="result_create"),
    path(
        "result/<int:pk>/", DiagnosticResultDetailView.as_view(), name="result_detail"
    ),
    path(
        "result/<int:pk>/update/",
        DiagnosticResultUpdateView.as_view(),
        name="result_update",
    ),
    path(
        "result/<int:pk>/delete/",
        DiagnosticResultDeleteView.as_view(),
        name="result_delete",
    ),
]
