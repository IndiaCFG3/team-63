# https://github.com/IndiaCFG3/team-63
from django.shortcuts import render, redirect
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
from django.contrib import messages

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

    return render(request, "users/signup.html")

@login_required
def custom_logout(request):
	logout(request)
	return HttpResponse("You have successfully Logged out from the system")


def home(request):

	return render(request, "users/index.html")


def login(request):

	return render(request, "users/login.html")

def show_mobilizers_under_me(request):

    loggedin_user = request.user

    loggedin_user = Application_User.objects.get(user = loggedin_user)

    all_mobilizers = None

    if loggedin_user.type_of_user == 'Manager' :

        loggedin_user = request.user

        all_mobilizers = Manager_to_Mob.objects.get(manager = loggedin_user).all_mobilizers.all()

    return render(request, "users/show_mobilizers_under_me.html", {"all_mobilizers" : all_mobilizers})

class login_api(APIView):

    def post(self, request):

        username = request.data["username"]
        password = request.data["password"]

        find_user = authenticate(username=username,password=password)

        if find_user is None : 
            messages.error(request, "Invalid Credentials !")
            return redirect("custom_login")

        else :

            login(request,find_user)
            return redirect("main-hello")

    def get(self, request):

        return render(request, "users/login.html")

def create_task_manager(request):

    return render(request, "users/manager1.html")

class create_task(APIView):

    def post(self, request):

        taskcreator = request.user
        taskname = request.data["taskname"]
        description = request.data["description"]
        fromduration = request.data["fromduration"]
        toduration = request.data["toduration"]
        maxnumber = request.data["maxnumber"]

        new_task = Task(
            taskcreator = taskcreator,
            taskname = taskname,
            description = description,
            fromduration = fromduration,
            toduration = toduration,
            maxnumber = maxnumber
        )

        new_task.save()

        messages.success(request, "Task Added!")

        return redirect("create_task_manager")

def signup(request):
    return render(request, "users/signup.html")


def show_all_tasks(request):

    all_tasks = Task.objects.all()

    context_dict = {
        "all_tasks" : all_tasks
    }

    return render(request,"users/all_tasks.html",context_dict)

def add_mobilizer(request):

    return render(request, "users/manager4.html")

def view_progress(request):

    return render(request, "users/manager3.html")

def manager4(request):
    return render(request, "users/manager4.html")