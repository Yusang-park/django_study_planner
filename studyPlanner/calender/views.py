from django.shortcuts import render, redirect

# Create your views here.
def calender(request):
    return render(request, 'calender.html')