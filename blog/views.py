from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
