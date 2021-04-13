from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Point
from .serializers import PointSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    point= PointSerializer()
    point_serializer= point.create(validated_data=pythondata)


def point_detail(request,pk):
    p = Point.objects.get(id=pk)
    serializer = PointSerializer(p)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def point_list(request):
    p = Point.objects.all()
    serializer = PointSerializer(p, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


