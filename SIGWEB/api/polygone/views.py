from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Polygone
from .serializers import PolygoneSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    polygone= PolygoneSerializer()
    polygone_serializer= polygone.create(validated_data=pythondata)


def polygone_detail(request,pk):
    p = Polygone.objects.get(id=pk)
    serializer = PolygoneSerializer(p)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def polygone_list(request):
    p = Polygone.objects.all()
    serializer = PolygoneSerializer(p, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



from django.shortcuts import render

# Create your views here.
