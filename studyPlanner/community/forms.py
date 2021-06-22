from django import forms
from .models import Comment, Write

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
