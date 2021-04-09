from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = UserSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')



def user_detail(request,pk):
    u = User.objects.get(id=pk)
    # print(u)
    serializer = UserSerializer(u)
    # print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def user_list(request):
    u = User.objects.all()
    # print(u)
    serializer = UserSerializer(u, many=True)
    # print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    user = UserSerializer()
    article_serializer = user.create(validated_data=pythondata)
