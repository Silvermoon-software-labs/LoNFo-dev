from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    
    url(r'^details/$', "lnf.views.Lnf_Detail"),
]