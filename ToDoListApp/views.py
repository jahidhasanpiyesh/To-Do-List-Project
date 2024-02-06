from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def u_register(request):
    fm = UserCreationForm()
    return render(request, 'ToDoListApp/register.html',{'fm':fm})