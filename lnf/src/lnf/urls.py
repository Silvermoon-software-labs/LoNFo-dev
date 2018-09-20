from django.conf.urls import url
from django.contrib import admin

from .views import(
      Lnf_Detail,
      Homepage ,
	)
urlpatterns = [
    
    url(r'^details/$', Lnf_Detail),
    url(r'^homepage/$', Homepage),

]