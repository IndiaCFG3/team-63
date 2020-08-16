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
from .forms import LoginForm


