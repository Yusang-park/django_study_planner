from .models import Profile, Todothing
from django.shortcuts import redirect, render, get_object_or_404
from .forms import DailyForm, TodothingForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def diary(request):
    user = request.user
    d_day = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        daily_form = DailyForm(request.POST)
        # todothing_form = TodothingForm(request.POST)
        if daily_form.is_valid():
            # todothing_form.save()
            daily_form.save()
            return redirect('diary:diary')
    daily_form = DailyForm()
    # todothing
    todo_lists = Todothing.objects.all()
    todo_form = TodothingForm()
    return render(request, 'diary_main.html',{
        "daily_form":daily_form,
        "todothing_form":todothing_form,
        "user":user,
        "d_day":d_day,
        "todo_lists":todo_lists,
        "todo_form":todo_form,
        } )

def setDday(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('diary:setDday')
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "set_dday.html",{"profile_form":profile_form})


# todolist 추가하기
def addTodo(request):
    if request.method == 'POST':
        todo_form = TodothingForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('diary:diary')
    else:
        todo_form = TodothingForm()
    return render(request, 'diary:diary_main', {'todo_form':todo_form})

# todolist 항목 체크하기 
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