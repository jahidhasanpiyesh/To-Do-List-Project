"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from coreapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.us_login, name='login'),
    path('logout/', views.us_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('deshbord/', views.deshbord, name='deshbord'),
    path('remove/<int:id>/', views.PostRemove, name='remove'),
    path('add/', views.Postadd, name='add'),
    path('update/<int:id>/', views.Postupdate, name='update'),
    path('search/', views.search, name='search'),
]

