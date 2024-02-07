from django.shortcuts import render, HttpResponseRedirect
from .forms import userforms, loginforms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def us_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = loginforms(request=request, data= request.POST)
            if fm.is_valid():
                u_name = fm.cleaned_data['username']
                u_pass = fm.cleaned_data['password']
                user = authenticate(username= u_name, password= u_pass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/deshbord/')
        else:           
            fm = loginforms()
        return render(request, 'coreapp/login.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/deshbord/')
    
def us_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        fm = userforms(request.POST)
        if fm.is_valid():
            fm.save()
            fm= userforms()
    else:
        fm = userforms()
    return render(request, 'coreapp/register.html', {'fm':fm})

def deshbord(request):
    if request.user.is_authenticated:
        return render(request, 'coreapp/deshbord.html')
    else:
        return HttpResponseRedirect('/login/')