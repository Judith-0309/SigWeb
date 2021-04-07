from django.shortcuts import render
from django.shortcuts import render
from .models import Compte
from .serializers import CompteSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse



def compte_detail(request,pk):
    c = Compte.objects.get(id=pk)
    serializer = CompteSerializer(c)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def compte_list(request):
    c = Compte.objects.all()
    serializer = CompteSerializer(c, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



