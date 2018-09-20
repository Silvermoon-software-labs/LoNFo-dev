from django.conf.urls import url
from django.contrib import admin

from .views import(
      dummy,
      landing,
    )
urlpatterns = [
    url(r'^dummy/$', dummy),
    url('$', landing),
]
