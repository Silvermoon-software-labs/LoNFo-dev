from django.conf.urls import url
from django.contrib import admin

from .views import (
      PostListAPIView
    )
urlpatterns = [
    url(r'^dummy/$', PostListAPIView.as_view()),
    url(r'^$', landing),
]
