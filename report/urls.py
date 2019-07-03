"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from .views import *

urlpatterns = [
    path('', index_page, name='index_page'),
    path('reports/', report_list, name='report_list'), 
    path('reports/<str:slug>/edit/', ReportUpdate.as_view(), name='edit_report'),
    path('reports/<str:slug>/delete/', ReportDelete.as_view(), name='delete_report'),
    path('reports/<str:slug>', ReportDetail.as_view(), name='report_url'),
    path('create_report/', ReportCreate.as_view(), name='create_report'),
]
