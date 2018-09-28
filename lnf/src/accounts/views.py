from django.shortcuts import render
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .form import UserLoginForm
# Create your views here.

def login_view(requests):
	title = "Login" 
	form = UserLoginForm(requests.Post or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
	
	context = {
		"title" : title,
		"form" : form,
	}

	return render(requests, "login_page.html", context)


def login_view(requests):
	return render(requests, "login_page.html", {})


def login_view(requests):
	return render(requests, "login_page.html", {})