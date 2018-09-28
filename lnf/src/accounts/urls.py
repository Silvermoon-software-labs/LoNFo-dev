from django.conf.urls import url
from django.contrib import admin

from .views import (
      login_view,
      register_page,
      logout_view
    )
urlpatterns = [
    url(r'^login/$', login_view),
    url(r'^register/$', register_page  ),

    #url(r'^logout/$', logout_view, name='logout'),
    #url(r'^$', landing),
]
