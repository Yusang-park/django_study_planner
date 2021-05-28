from .models import Daily,Todothing, Checkpoint
from django import forms

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['goal','date','studytime','feelings','d_day']

class TodothingForm(forms.ModelForm):
    class Meta:
        models = Todothing
        fields = ['todothing','checkbox']

class CheckpointForm(forms.ModelForm):
    class Meta:
        models = Checkpoint
        fields = ['checkthing']