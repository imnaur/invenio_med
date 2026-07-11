from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from catalog.forms import ServiceForm
from catalog.models import Service


class ServiceCreateView(PermissionRequiredMixin, CreateView):
    """Класс для создания услуги"""

    model = Service
    form_class = ServiceForm
    template_name = "catalog/service_create.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.add_service"


class ServiceListView(ListView):
    """Класс для вывода списка услуг"""

    model = Service
    template_name = "catalog/service_list.html"
    context_object_name = "services"
    paginate_by = 6


class ServiceDetailView(DetailView):
    """Класс для детали услуги"""

    model = Service
    template_name = "catalog/service_detail.html"
    context_object_name = "service"


class ServiceUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс для обновления услуги"""

    model = Service
    form_class = ServiceForm
    template_name = "catalog/service_update.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.change_service"


class ServiceDeleteView(PermissionRequiredMixin, DeleteView):
    """Класс для удаления услуги"""

    model = Service
    template_name = "catalog/service_confirm_delete.html"
    success_url = reverse_lazy("catalog:service_list")
    context_object_name = "service"
    permission_required = "catalog.delete_service"
