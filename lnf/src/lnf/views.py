from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import LostNFound


def dummy(requests):

    queryset = LostNFound.objects.all()
    query = requests.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(Name__icontains=query) |
            Q(Lost_Found_Product__icontains=query) |
            Q(Location__contains=query)
            )

    details = {
        "object_list": queryset
    }
        
    return render(requests, "Lnf_Detail.html", details)


def landing(requests):
    return render(requests, "index.html", {})
