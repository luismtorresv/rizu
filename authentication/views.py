from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import OpenStackUserRegistrationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("front_page_index")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        form = OpenStackUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("front_page_index")
    else:
        form = OpenStackUserRegistrationForm()

    return render(request, "register.html", {"form": form})
