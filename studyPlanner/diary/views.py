from tabnanny import check
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect

from .models import Profile
from django.shortcuts import redirect, render
from .forms import DailyForm, TodothingForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import auth
import datetime
from datetime import date
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
def diary(request):
    today = date.today()
    print('today',today)
    # todothing
    # daily = Daily.objects.filter(user = request.user)
    #서버의 write 클래스 정보를 모두 가져온다.
    user = request.user
    if user.is_authenticated:
        d_day = Profile.objects.get(user = request.user)
        try:
            todo_lists = Todothing.objects.filter(user=request.user,date = today)
            daily = Daily.objects.get(user = request.user)
        except Daily.DoesNotExist :
            daily = None
        except Todothing.DoesNotExist :
            todo_lists = None
    else:
        return render(request,'no_login.html')
    todo_form = TodothingForm()       
    daily_form = DailyForm()
    # if request.method == 'POST':
    #     daily_form = DailyForm(request.POST)
    #     if daily_form.is_valid():
    #         daily_form = daily_form.save(commit=False)
    #         daily_form.user = request.user
    #         daily_form.save()
    #         return redirect('diary:diary')
    # daily_form = DailyForm()
    return render(request, 'diary_main.html',{"daily_form":daily_form,"user":user,"d_day":d_day, 'todo_lists' : todo_lists,
        'todo_form' : todo_form, 'daily' : daily } )
    

def setDiary(request):
    today = date.today()
    print('today',today)
    user = request.user
    if user.is_authenticated:
        d_day = Profile.objects.get(user = request.user)
        daily = Daily.objects.filter(user=request.user, date = today).first()
    else:
        d_day = None
        daily = None
    if request.method == 'POST':
        daily_form = DailyForm(request.POST, instance=daily)
        if daily_form.is_valid():
            daily_form = daily_form.save(commit=False)
            daily_form.user = request.user
            daily_form.save()
            return redirect('diary:diary')
    else:
        daily_form = DailyForm(instance=daily)
    return render(request, 'set_diary.html', {'daily_form': daily_form, 'daily':daily, "d_day":d_day })


def addTodo(request):
    today = date.today()
    print('today',today)
    if request.method == 'POST':
        todo_form = TodothingForm(request.POST)
        if todo_form.is_valid():
            todo_form = todo_form.save(commit=False)
            todo_form.user = request.user
            todo_form.save()
            return redirect('diary:diary')
    else:
        todo_form = TodothingForm()
    return render(request, "diary:diary_main", {'todo_form' : todo_form})


# 체크 박스를 사용하는 것이 아니라 링크를 사용해서.
@csrf_exempt
def changeTodo(request, id):
    id = int(id)
    todo_list = get_object_or_404(Todothing, pk=id)
    if todo_list.checkbox == True:
        todo_list.checkbox = False
    else:
        todo_list.checkbox = True
    todo_list.save()
    return redirect('diary:diary')


@csrf_exempt
def deleteTodo(request, id):
    id = int(id)
    todo_list = get_object_or_404(Todothing, pk=id)
    todo_list.delete()
    return redirect('diary:diary')
    







        



    

        
    
    

def setDday(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('diary:diary')
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "set_dday.html",{"profile_form":profile_form})


def logout(request):
    auth.logout(request)
    return redirect('diary:diary')
