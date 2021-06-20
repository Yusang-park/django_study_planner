from django.forms import widgets
from .models import Daily,Todothing, Checkpoint,Profile
from django import forms
from django.forms import widgets
class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['goal','studytime_h','studytime_m','feelings']


class TodothingForm(forms.ModelForm):
    class Meta:
        model = Todothing
        fields = ['todothing','checkbox']

class CheckpointForm(forms.ModelForm):
    class Meta:
        model = Checkpoint
        fields = ['checkthing']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['goal_day']
        widgets = {
            'goal_day':widgets.SelectDateWidget,
        }