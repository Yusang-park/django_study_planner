from django.shortcuts import render, redirect
from django.utils import timezone


# Create your views here.
def calender(request):
    year = timezone.now().year
    month = timezone.now().month
    properties = {'year': year, 'month': month, }
    return render(request, 'calender.html', properties)


def changeMonth(request, year,month):
    return render(request, 'calender.html', properties)
