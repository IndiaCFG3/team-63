"""Anudip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name = 'home'),
    path('signup/', users_views.signup, name='signup'),
    path('signin/', users_views.login_request, name='login_request'),
    path('logout/', users_views.custom_logout, name = 'logout'),
    path('login/', users_views.login_api.as_view(), name = 'login'),
    path('show_mobilizers_under_me', users_views.show_mobilizers_under_me, name = 'show_mobilizers_under_me'),
    path('create_task/', users_views.create_task.as_view(), name = 'create_task'),
    path('create_task_manager/', users_views.create_task_manager, name = 'create_task_manager'),
    path('show_all_tasks/', users_views.show_all_tasks, name = 'show_all_tasks'),
    path('view_progress/', users_views.view_progress, name = 'view_progress'),
    path('add_mobilizer/', users_views.add_mobilizer, name = 'add_mobilizer'),
    path('manager4/',users_views.manager4,name='manager-4')]