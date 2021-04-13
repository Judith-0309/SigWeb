from rest_framework.parsers import JSONParser
import io
from .models import DonneesRaster
from .serializers import DonneesRasterSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):

    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    donneesRaster = DonneesRasterSerializer()
    donnees_serializer = donneesRaster.create(validated_data=pythondata)


def donneesRaster_detail(request,pk):
    v = DonneesRaster.objects.get(id=pk)
    serializer = DonneesRasterSerializer(v)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def donneesRaster_list(request):
    v = DonneesRasterSerializer.objects.all()
    serializer = DonneesRasterSerializer(v, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



