from . import views
from django.urls import path

app_name = "diary"

urlpatterns = [
    path('', views.diary, name="diary"),
    path('setDday/',views.setDday, name='setDday'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('checkedTodo', views.checkedTodo, name='checkedTodo'),
]