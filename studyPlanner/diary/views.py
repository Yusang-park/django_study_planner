from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from .decorators import diary_ownership_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from favoriteapp.forms import FavoriteForm

# Create your views here.
has_ownership = [diary_ownership_required,login_required]

@method_decorator(has_ownership,'get')
class DiaryDetailView(DetailView):
    model = User
    context_object_name = 'target_diary'
    template_name = 'diary/index.html'
    # def get_context_data(self,**kwargs):

