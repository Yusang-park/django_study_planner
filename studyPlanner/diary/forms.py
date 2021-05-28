from .models import Daily,Todothing, Checkpoint
from django import forms

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['goal','studytime','feelings','d_day']

class TodothingForm(forms.ModelForm):
    class Meta:
        model = Todothing
        fields = ['todothing','checkbox']

class CheckpointForm(forms.ModelForm):
    class Meta:
        model = Checkpoint
        fields = ['checkthing']