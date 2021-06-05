from django.views.generic.edit import DeleteView
from .forms import FavoriteForm
from django.shortcuts import render
from django.urls import reverse
from .models import Favorite
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
# Create your views here.
@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class FavoriteCreateView(CreateView):
    model = Favorite
    form_class = FavoriteForm
    template_name = 'favoriteapp/create.html'

    def form_valid(self,form):
        temp_form = form.save(commit=False)
        temp_form.user = self.request.user
        temp_form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary:detail',kwargs={'pk':self.object.user.pk})

@method_decorator(login_required,'post')
class FavoriteDeleteView(DeleteView):
    model = Favorite
    context_object_name = 'target_favorite'
    template_name = 'favoriteapp/delete.html'

    def get_success_url(self):
        return reverse('diary:detail',kwargs={'pk':self.object.user.pk})