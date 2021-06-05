from django import forms
from django.db.models import fields
from .models import Favorite

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['title','link']