from django.http.response import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import Daily

def diary_ownership_required(func):
    def decorated(request,*args,**kwargs):
        diary = User.objects.get(pk=kwargs['pk'])
        if not diary == request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated
    