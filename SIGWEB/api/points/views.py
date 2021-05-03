from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from .models import Points
from .serializers import PointsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    point= PointsSerializer()
    point_serializer= point.create(validated_data=pythondata)


def point_detail(request,pk):
    p = Points.objects.get(id=pk)
    serializer = PointsSerializer(p)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def point_list(request):
    p = Points.objects.all()
    serializer = PointsSerializer(p, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


