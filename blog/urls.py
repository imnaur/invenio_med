from django.urls import path

from blog.views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                        BlogListView, BlogUpdateView)

app_name = "blog"

urlpatterns = [
    path("services/", BlogListView.as_view(), name="blog_list"),
    path("service/create/", BlogCreateView.as_view(), name="blog_create"),
    path("service/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("service/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("service/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
]
