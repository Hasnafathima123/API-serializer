from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from . models import Address
from . serializer import AddressSerializer
 
def index (request):
    address=Address.objects.all()
    serilaizer=AddressSerializer(address, many=True)
    return JsonResponse(serilaizer.data, safe=False)
def detial(request,id):
    address=Address.objects.get(id=id)
    serializer=AddressSerializer(address)
    return JsonResponse(serializer.data, safe=False)