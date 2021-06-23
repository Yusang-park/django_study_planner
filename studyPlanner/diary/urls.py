from django.utils.translation import check_for_language
from . import views
from django.urls import path

app_name = "diary"

urlpatterns = [
    path('', views.diary, name="diary"),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('changeTodo/<int:id>/', views.changeTodo, name='changeTodo'),
    path('deleteTodo/<int:id>/', views.deleteTodo, name='deleteTodo'),
    path('setDday/',views.setDday, name='setDday'),
    path('logout/', views.logout, name='logout'),
    path('setDiary/', views.setDiary, name='setDiary'),
    path('diary/<int:year>/<int:month>/<int:day>/', views.changed_diary, name="changed_diary"),
]