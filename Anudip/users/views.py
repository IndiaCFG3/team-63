# https://github.com/IndiaCFG3/team-63

from django.shortcuts import render
import os
import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.html import format_html
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if request.method == "POST":
	    form = RegisterForm(request.POST)
	    if form.is_valid():
	        form.save()
    form = RegisterForm()
    return render(request = request,template_name = "users/register.html",context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "users/login.html",
                    context={"form":form})
@login_required
def formL(request):
    if request.method == 'POST':
        form = login_request(request.POST)

    else:
        form = login_request()
    context_dict = {
        "form":form
    }

    return render(request, "users/login.html")


@login_required
def formR(request):
    if request.method == 'POST':
        form = register(request.POST)

    else:
        form = register()
    context_dict = {
        "form":form
    }

    return render(request, "users/register.html")