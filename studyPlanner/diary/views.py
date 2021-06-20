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

# Create your views here.
def diary(request):
    # todothing
    todo_lists = Todothing.objects.all()
    todo_form = TodothingForm()
    #서버의 write 클래스 정보를 모두 가져온다.

    return render(request, 'diary_main.html', {
        'todo_lists' : todo_lists,
        'todo_form' : todo_form,
    })

def addTodo(request):
    if request.method == 'POST':
        todo_form = TodothingForm(request.POST)
        if todo_form.is_valid():
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
        # 체크된 것을 True로 바꿔주기
        todo_list.checkbox = True
        todo_list.save() # 모델의 필드 저장
    return redirect('diary:diary')


        



    

        
    
    return render(request, 'diary_main.html')
    user = request.user
    if user.is_authenticated:
        d_day = Profile.objects.get(user = request.user)
             
    else:
        d_day = 0       
    if request.method == 'POST':
        daily_form = DailyForm(request.POST)
        todothing_form = TodothingForm(request.POST)
        if daily_form.is_valid():
            todothing_form.save()
            daily_form.save()
            return redirect('diary:diary')
    daily_form = DailyForm()
    todothing_form = TodothingForm()
    return render(request, 'diary_main.html',{"daily_form":daily_form,"todothing_form":todothing_form,"user":user,"d_day":d_day} )

def setDday(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('diary:setDday')
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "set_dday.html",{"profile_form":profile_form})


def logout(request):
    auth.logout(request)
    return redirect('diary:diary')
