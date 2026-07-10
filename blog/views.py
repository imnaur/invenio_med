from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import BlogFormView

from .models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/blog_create.html"
    form_class = BlogFormView
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.add_blog"


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    paginate_by = 6
    context_object_name = "blogs"
    permission_required = "blog.view_blog"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    permission_required = "blog.change_blog"


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog/blog_update.html"
    form_class = BlogFormView
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.change_blog"


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")
    permission_required = "blog.delete_blog"
