from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,related_name='favorite')
    title = models.CharField(max_length=100)
    link = models.URLField(null=False)

    def __str__(self):
        return self.user.favorite