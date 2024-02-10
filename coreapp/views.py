from django.shortcuts import render, HttpResponseRedirect
from .forms import userforms, loginforms, add_post_forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import add_post


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
        post = add_post.objects.all()
        return render(request, 'coreapp/deshbord.html',{'fm':post})
    else:
        return HttpResponseRedirect('/login/')

def Postadd(request):
    if request.method == 'POST':
        fm = add_post_forms(request.POST)
        if fm.is_valid():
            fm.save()
            fm = add_post_forms()
    else:
        fm = add_post_forms()
    return render(request,'coreapp/postadd.html',{'fm':fm})

def Postupdate(request):
    return render(request, 'coreapp/update.html')

def PostRemove(request,id):
    if request.method =='POST':
        pi = add_post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/deshbord/')
    else:
        return render(request, 'coreapp/remove.html')