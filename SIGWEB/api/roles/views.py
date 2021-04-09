import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Role
from .serializers import RoleSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse




@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    role = RoleSerializer()
    role_serializer = role.create(validated_data=pythondata)


def role_detail(request, pk):
    r = Role.objects.get(id=pk)
    serializer = RoleSerializer(r)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def role_list(request):
    r = Role.objects.all()
    serializer = RoleSerializer(r, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
