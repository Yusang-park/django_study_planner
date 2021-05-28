from django.shortcuts import render,redirect
from django.contrib import auth

# Create your views here.
def diary(request):
    #서버의 write 클래스 정보를 모두 가져온다.
    return render(request, 'diary_main.html')

def logout(request):
    auth.logout(request)
    return redirect('diary:diary')