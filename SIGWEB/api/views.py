
from .user.views import user_create
from .user.views import user_detail
from .user.views import user_list
from django.views import View
from requests import request

class MyViews(View):
    def get(self,request, *args, **kwargs):
        return user_list(request)
    def get(self,request,*args, **kwargs):
        return user_create(request)