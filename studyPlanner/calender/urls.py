from . import views
from django.urls import path

app_name = "calender"

urlpatterns = [
    path('calender/', views.calender, name="calender"),

    # path('signin/', views.signin, name="signin")
]