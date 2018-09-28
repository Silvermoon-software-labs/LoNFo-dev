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
    print(requests.user.is_authenticated())
    title = "Login" 
    form = UserLoginForm(requests.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(requests,user)
        print(requests.user.is_authenticated())
	# context = {
	# 	"title" : title,
	# 	"form" : form,
	# }

    return render(requests, "login_page.html", {"form":form, "title":title})


def register_page(requests):
    return render(requests, "login_page.html", {})


def logout_view(requests):
    return render(requests, "login_page.html", {})