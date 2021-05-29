from . import views
from django.urls import path

app_name = "calender"

urlpatterns = [
    path('', views.calender, name="calender"),
    path('<int:year>/<int:month>/', views.change_calender, name="change_calender"),
    
]