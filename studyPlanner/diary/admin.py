from django.contrib import admin
from .models import Todothing
# Register your models here.
admin.site.register(Todothing)
from .models import *

# Register your models here.
admin.site.register(Daily)
admin.site.register(Todothing)
admin.site.register(Profile)
