from . import views
from django.urls import path

app_name = "diary"

urlpatterns = [
    path('', views.diary, name="diary"),
    path('logout/', views.logout, name='logout')
]