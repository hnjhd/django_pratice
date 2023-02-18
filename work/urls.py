"""work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app01 import views
urlpatterns = [  
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('event/add/',views.event_add),
    path('event/delete/',views.event_delete),
    path('event/list/',views.event_list),
    path('event/<int:nid>/edit/',views.event_edit),
    path('school/add/',views.school_add),
    path('country/add/',views.country_add),
    path('major/add/',views.major_add),
    path('school/delete/',views.school_delete),
    path('country/delete/',views.country_delete),
    path('major/delete/',views.major_delete),
    path('school/list/',views.school_list),
    path('country/list/',views.country_list),
    path('major/list/',views.major_list),
    path('user_event/',views.user_event),
    path('my_event/',views.my_event),
    path('my_event/delete/',views.my_event_delete),
 ]
