from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.forms import ServiceForm
from catalog.models import Service
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)


class ServiceCreateView(PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "catalog/service_create.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.add_service"


class ServiceListView(ListView):
    model = Service
    template_name = "catalog/service_list.html"
    context_object_name = "services"
    paginate_by = 6


class ServiceDetailView(DetailView):
    model = Service
    template_name = "catalog/service_detail.html"
    context_object_name = "service"


class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "catalog/service_update.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.change_service"


class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
    model = Service
    template_name = "catalog/service_confirm_delete.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.delete_service"
