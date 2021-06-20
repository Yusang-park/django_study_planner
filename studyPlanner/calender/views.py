from django.shortcuts import render, redirect
from django.utils import timezone


# Create your views here.
def calender(request):
    year = timezone.now().year
    month = timezone.now().month
    context = {'year': year, 'month': month, 'previous_year' : year-1, 'next_year' : year+1}
    return render(request, 'calender.html', context)


def change_calender(request, year, month):
    context={'year' : year, 'month' : month, 'previous_year' : year-1, 'next_year' : year+1}
    return render(request, 'calender.html',context)

