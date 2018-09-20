from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import LostNFound


def dummy(requests):
    queryset = LostNFound.objects.all()
    details = {
        "object_list": queryset
    }
    return render(requests, "Lnf_Detail.html", details)


def landing(requests):
    return render(requests, "index.html", {})
