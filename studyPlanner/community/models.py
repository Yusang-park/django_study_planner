from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Write(models.Model):
    title= models.CharField(max_length=50)
    user= models.ForeignKey(User,related_name='write',on_delete=CASCADE,null=True)
    mainphoto = models.ImageField(null=True,blank=True)
    contents= models.TextField()
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey(Write,related_name='comment',on_delete=CASCADE)
    content= models.TextField(max_length=200)
    user = models.ForeignKey(User,related_name='comment',on_delete=CASCADE)

    def __str__(self):
        return self.post.title

# Create your models here.
