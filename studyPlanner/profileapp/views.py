from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth
# Create your views here.
def login(request):
    return render(request,'profileapp/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'profileapp/login.html')