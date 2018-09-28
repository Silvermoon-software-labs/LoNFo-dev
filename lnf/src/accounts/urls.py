from django.conf.urls import url
from django.contrib import admin

from .views import (
      login_view
    )
urlpatterns = [
    url(r'^login/$', login_view),
    #url(r'^$', landing),
]
