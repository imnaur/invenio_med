from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from users.models import CustomUser

from .forms import AppointmentForm, DiagnosticResultForm
from .models import Appointment, DiagnosticResult
from .tasks import send_appointment_email_task


# ----------------------------------Appointment------------------------------------------


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """Класс по созданию новой записи"""

    model = Appointment
    form_class = AppointmentForm
    template_name = "appointments/appointment_create.html"
    context_object_name = "appointment"
    success_url = reverse_lazy("appointments:appointment_list")

    def form_valid(self, form):
        """Метод отправляет письмо подтверждения на почту админам"""
        form.instance.patient = self.request.user
        form.instance.status = "created"
        response = super().form_valid(form)

        appointment = form.instance
        user = self.request.user

        send_appointment_email_task.delay(
            patient_name=f"{user.first_name} {user.last_name}",
            patient_email=user.email,
            patient_phone=str(user.phone_number),
            appointment_date_str=appointment.date.strftime("%d.%m.%Y в %H:%M"),
        )

        messages.success(self.request, "Запись создана! Администратор скоро с Вами свяжется.")
        return response


class AppointmentListView(LoginRequiredMixin, ListView):
    """Класс выводит все записи"""

    model = Appointment
    template_name = "appointments/appointment_list.html"
    context_object_name = "appointments"
    paginate_by = 6

    def get_queryset(self):
        """Метод возвращает все записи для админов и докторов, и личные для пациентов"""
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return Appointment.objects.all()
        appointments = Appointment.objects.filter(patient=self.request.user)
        return appointments


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    """Класс о деталях определенной записи"""

    model = Appointment
    template_name = "appointments/appointment_detail.html"
    context_object_name = "appointment"

    def get_queryset(self):
        """Метод возвращает все записи для админов и докторов, и личные для пациентов"""
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return Appointment.objects.all()
        appointments = Appointment.objects.filter(patient=self.request.user)
        return appointments

    def get_context_data(self, **kwargs):
        """Метод выводит слаг контактов"""
        context = super().get_context_data(**kwargs)
        context["page_slug"] = "contacts"
        return context


class AppointmentUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс по обновлению записи"""
    model = Appointment
    template_name = "appointments/appointment_update.html"
    context_object_name = "appointment"
    form_class = AppointmentForm
    success_url = reverse_lazy("appointments:appointment_list")
    permission_required = "appointments.change_appointment"

    def get_context_data(self, **kwargs):
        """Метод выводит имя и фамилию пациента"""
        context = super().get_context_data(**kwargs)
        context["first_name"] = self.object.patient.first_name
        context["last_name"] = self.object.patient.last_name
        return context


class AppointmentDeleteView(PermissionRequiredMixin, DeleteView):
    """Класс для удаления записи"""
    model = Appointment
    template_name = "appointments/appointment_confirm_delete.html"
    context_object_name = "appointment"
    success_url = reverse_lazy("appointments:appointment_list")
    permission_required = "appointments.delete_appointment"

    def get_context_data(self, **kwargs):
        """"Метод выводит имя услуги"""
        context = super().get_context_data(**kwargs)
        context["service_name"] = self.object.service.name
        return context


# ----------------------------------DiagnosticResult------------------------------------------


class DiagnosticResultCreateView(LoginRequiredMixin, CreateView):
    model = DiagnosticResult
    form_class = DiagnosticResultForm
    template_name = "appointments/result_create.html"
    context_object_name = "result"
    success_url = reverse_lazy("appointments:result_list")


class DiagnosticResultListView(LoginRequiredMixin, ListView):
    model = DiagnosticResult
    template_name = "appointments/result_list.html"
    context_object_name = "results"
    paginate_by = 6

    def get_queryset(self):
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return DiagnosticResult.objects.all()
        return DiagnosticResult.objects.filter(
            appointment__patient=self.request.user
        ).select_related("appointment")


class DiagnosticResultDetailView(LoginRequiredMixin, DetailView):
    model = DiagnosticResult
    template_name = "appointments/result_detail.html"
    context_object_name = "result"

    def get_queryset(self):
        """Метод возвращает результаты для админов и докторов, и личные для пациентов"""
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return DiagnosticResult.objects.all()
        results = DiagnosticResult.objects.filter(appointment__patient=self.request.user)
        return results


class DiagnosticResultUpdateView(PermissionRequiredMixin, UpdateView):
    model = DiagnosticResult
    template_name = "appointments/result_update.html"
    context_object_name = "result"
    form_class = DiagnosticResultForm
    success_url = reverse_lazy("appointments:result_list")
    permission_required = "appointments.change_diagnosticresult"

    def get_queryset(self):
        """Метод возвращает результаты для админов и докторов, и личные для пациентов"""
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return DiagnosticResult.objects.all()
        results = DiagnosticResult.objects.filter(appointment__patient=self.request.user)
        return results


class DiagnosticResultDeleteView(PermissionRequiredMixin, DeleteView):
    model = DiagnosticResult
    template_name = "appointments/result_confirm_delete.html"
    context_object_name = "result"
    success_url = reverse_lazy("appointments:result_list")
    permission_required = "appointments.delete_diagnosticresult"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_name"] = self.object.appointment.service.name
        return context

    def get_queryset(self):
        """Метод возвращает результаты для админов и докторов, и личные для пациентов"""
        user: CustomUser = self.request.user
        if user.is_superuser or user.is_doctor or user.is_staff:
            return DiagnosticResult.objects.all()
        results = DiagnosticResult.objects.filter(appointment__patient=self.request.user)
        return results
