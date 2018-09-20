from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Lnf_Detail(requests):
	return render(requests, "Lnf_Detail.html", {})