from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BlogFormView
from .models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    """Класс для создания блога"""
    model = Blog
    template_name = "blog/blog_create.html"
    form_class = BlogFormView
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.add_blog"


class BlogListView(ListView):
    """Класс списка блога"""
    model = Blog
    template_name = "blog/blog_list.html"
    paginate_by = 6
    context_object_name = "blogs"
    permission_required = "blog.view_blog"


class BlogDetailView(DetailView):
    """Класс для детали блога"""
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    permission_required = "blog.change_blog"


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс для обновления блога"""
    model = Blog
    template_name = "blog/blog_update.html"
    form_class = BlogFormView
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.change_blog"


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    """Класс для удаления блога"""
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.delete_blog"
