from django.views.generic import ListView

from .models import Project


class ProjectListView(ListView):
    model = Project
    slug_field = "name"
    slug_url_kwarg = "name"
