from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Daily(models.Model):
    user = models.ForeignKey(User,related_name='daily',on_delete=CASCADE)
    goal = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    #The default form widget for this field is a single DateTimeInput.
    #The admin uses two separate TextInput widgets with JavaScript shortcuts.
    studytime = models.DateTimeField() 
    feelings = models.TextField()

    #The default form widget for this field is a DateInput.
    #The admin adds a JavaScript calendar, and a shortcut for “Today”
    d_day = models.DateField()

    #체크리스트, 할일은 자녀테이블로 알아서 연결돼있을것

    def __str__(self):
        return self.date

class Todothing(models.Model):
    day = models.ForeignKey(Daily,related_name='todothing',on_delete=CASCADE)
    todothing = models.CharField(max_length=50)

    #The default form widget for this field is CheckboxInput, or NullBooleanSelect if null=True.
    #The default value of BooleanField is None when Field.default isn’t defined.
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.todothing

class Checkpoint(models.Model):
    day = models.ForeignKey(Daily,related_name='checkpoint',on_delete=CASCADE)
    checkthing = models.CharField(max_length=100)

    def __str__(self):
        return self.checkthing