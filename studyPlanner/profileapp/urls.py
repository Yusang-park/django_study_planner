from django.urls import path
from .views import login,logout

app_name = 'profileapp'

urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]