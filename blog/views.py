from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    success_url = reverse_lazy("blog:blog_detail")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
