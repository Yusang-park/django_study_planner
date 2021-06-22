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
        d_day = None
        todo_lists = None
        daily = None
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


def checkedTodo(request):
    checked = request.POST.getlist('checked') # html에서 체크한 목록의 id값 리스트로 받아오기
    # 체크한 id값에 해당하는 checkbox = True로 수정하기
    for id in checked:
        id = int(id) # 리스트 내의 요소를 문자열에서 정수로 바꾸기
        todo_list = get_object_or_404(Todothing, pk=id)
        # True인 것은 False로, False인 것은 True로 바꿔주기
        if 'check' in request.POST: # update 버튼을 눌렀을 때
            if todo_list.checkbox == False:
                todo_list.checkbox = True
            else:
                todo_list.checkbox = False
            todo_list.save()
        elif 'delete' in request.POST: # delete 버튼을 눌렀을 때 
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
