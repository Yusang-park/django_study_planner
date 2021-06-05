from django.urls import path
from .views import FavoriteCreateView,FavoriteDeleteView

app_name = 'favoriteapp'

urlpatterns = [
    path('create/',FavoriteCreateView.as_view(),name='create'),
    path('delete/<int:pk>',FavoriteDeleteView.as_view(),name='delete')
]