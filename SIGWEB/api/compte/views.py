from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Compte
from .serializers import CompteSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .. import compte


@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    compte= CompteSerializer()
    article_serializer= compte.create(validated_data=pythondata)


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



