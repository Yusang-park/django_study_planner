from . import views
from django.urls import path

app_name = "diary"

urlpatterns = [
    path('', views.diary, name="diary"),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('checkedTodo', views.checkedTodo, name='checkedTodo'),
    path('setDday/',views.setDday, name='setDday'),
    path('logout/', views.logout, name='logout'),
    
]