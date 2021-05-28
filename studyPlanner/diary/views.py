from django.shortcuts import render
from .forms import DailyForm, TodothingForm

# Create your views here.
def diary(request):
    daily_form = DailyForm()
    todothing_form = TodothingForm()
    return render(request, 'diary_main.html',{"daily_form":daily_form,"todothing_form":todothing_form} )