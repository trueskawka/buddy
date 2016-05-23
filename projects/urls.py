# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),
]
