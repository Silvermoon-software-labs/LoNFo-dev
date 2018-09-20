from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import LostNFound

def Lnf_Detail(requests):
    queryset = LostNFound.objects.all()
    details = {
        "object_list" : queryset
    }
    return render(requests, "Lnf_Detail.html", details)