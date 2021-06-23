from django.utils import timezone
from .models import *

from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render,redirect


# Create your views here.
def calender(request):
    user = request.user
    
    
    year = timezone.now().year
    month = timezone.now().month
    today = timezone.now().day
    context = {'year': year, 'month': month, 'previous_year' : year-1, 'next_year' : year+1, 'today' : today, 'user' : user}
    return render(request, 'calender.html', context)


def change_calender(request, year, month):
    context={'year' : year, 'month' : month, 'previous_year' : year-1, 'next_year' : year+1}
    return render(request, 'calender.html',context)

