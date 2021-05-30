from .models import Profile
from django.shortcuts import redirect, render
from .forms import DailyForm, TodothingForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def diary(request):
    user = request.user
    d_day = Profile.objects.get(user = request.user)
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

