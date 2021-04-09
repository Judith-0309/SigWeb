from django.shortcuts import render
from .models import Donnees
from .serializers import DonneesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .. import donnees


@csrf_exempt
def donnees_create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    donnees = DonneesSerializer()
    donnees_serializer = donnees.create(validated_data=pythondata)



def donnees_detail(request,pk):
    d = Donnees.objects.get(id=pk)
    serializer = DonneesSerializer(d)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def donnees_list(request):
    d = Donnees.objects.all()
    serializer = DonneesSerializer(d, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

