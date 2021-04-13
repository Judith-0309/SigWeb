from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Ligne
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import LigneSerializer


@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    ligne= LigneSerializer()
    ligne_serializer = ligne.create(validated_data=pythondata)


def ligne_detail(request,pk):
    l = Ligne.objects.get(id=pk)
    serializer = LigneSerializer(l)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def ligne_list(request):
    l = Ligne.objects.all()
    serializer = LigneSerializer(l, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



from django.shortcuts import render

# Create your views here.
