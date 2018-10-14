from django.conf.urls import url
from django.contrib import admin

from lnf.api.views import (
      PostListAPIView,
    )
urlpatterns = [
    url(r'^', PostListAPIView.as_view(), name='dummy'),
    # url(r'^$', landing),
]