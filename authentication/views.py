from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import OpenStackUserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from Rizu.openStackCommunication import OpenStackCommunication

osc = OpenStackCommunication()


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            return redirect("front_page_index")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = OpenStackUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            osc.create_openstack_user(user=user)
            return redirect("front_page_index")
    else:
        form = OpenStackUserRegistrationForm()

    return render(request, "register.html", {"form": form})
