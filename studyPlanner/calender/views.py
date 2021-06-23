from django.utils import timezone
from .models import *
import json
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render,redirect
from datetime import date

from diary.models import Profile, Daily, Todothing

# Create your views here.
def calender(request):
    user = request.user
    

    today = date.today()
    
    # todothing
    # daily = Daily.objects.filter(user = request.user)
    #서버의 write 클래스 정보를 모두 가져온다.
    
    if user.is_authenticated:
        d_day = Profile.objects.get(user = request.user)
        try:
            todo_lists = Todothing.objects.filter(user=request.user)
            daily = Daily.objects.get(user = request.user)
            
        except Daily.DoesNotExist :
            daily = None
        
        except Todothing.DoesNotExist :
            todo_lists = None
            
    else:
        return render(request,'no_login.html')


    todo_lists_js = []

    for todo_list in todo_lists:
        todo_lists_js.append({'date':str(todo_list.date.year)+'/'+ str(todo_list.date.month)+'/'+ str(todo_list.date.day), 'checkBox':1 if todo_list.checkbox == True else 0, 'todo' : todo_list.todothing})



    # todo_lists_js = json.dumps(todo_lists_js)
    print(todo_lists_js)


    year = timezone.now().year
    month = timezone.now().month
    today = timezone.now().day
    context = {'year': year, 'month': month, 'previous_year' : year-1, 'next_year' : year+1, 'today' : today, 'user' : user
    
    ,'todo_lists_js' : todo_lists_js,
        'daily' : daily }
    return render(request, 'calender.html', context)


def change_calender(request, year, month):

    user = request.user
    

    
    # todothing
    # daily = Daily.objects.filter(user = request.user)
    #서버의 write 클래스 정보를 모두 가져온다.
    
    if user.is_authenticated:
        d_day = Profile.objects.get(user = request.user)
        try:
            todo_lists = Todothing.objects.filter(user=request.user)
            daily = Daily.objects.get(user = request.user)
            
        except Daily.DoesNotExist :
            daily = None
        
        except Todothing.DoesNotExist :
            todo_lists = None
            
    else:
        return render(request,'no_login.html')


    todo_lists_js = []

    for todo_list in todo_lists:
        todo_lists_js.append({'date':str(todo_list.date.year)+'/'+ str(todo_list.date.month)+'/'+ str(todo_list.date.day), 'checkBox':1 if todo_list.checkbox == True else 0, 'todo' : todo_list.todothing})



    # todo_lists_js = json.dumps(todo_lists_js)
    print(todo_lists_js)
    context={'year' : year, 'month' : month, 'previous_year' : year-1, 'next_year' : year+1 ,'todo_lists_js' : todo_lists_js,
        'daily' : daily,'today':0 }
    return render(request, 'calender.html',context)

