from . import views
from django.urls import path


app_name = "diary"

urlpatterns = [
    path('diary/<int:pk>', views.DiaryDetailView.as_view(), name="detail"),
]