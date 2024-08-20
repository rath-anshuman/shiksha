from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Routine,RoutineSerializers

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def routine(request):
    if request.method == 'GET':
        rout=Routine.objects.all()
        serializer=RoutineSerializers(rout,many=True)
        return JsonResponse({'Routine :': serializer.data})

    if request.method == 'POST':
        # json=JSONParser().parse(request)
        serializer = RoutineSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'New Routine :':serializer.data})
        else :
            return JsonResponse({'message':serializer.errors})



@api_view(['GET','PUT','DELETE'])
def routinedtl(request,pk):
    try:
        rout=Routine.objects.get(pk=pk)
    except Routine.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        srlz=RoutineSerializers(rout)
        return JsonResponse({f'Routine/{pk}':srlz.data})
    
    if request.method == 'PUT':
        srlz=RoutineSerializers(rout,data=request.data)
        if srlz.is_valid():
            srlz.save()
            return JsonResponse({f'Update/{pk} :':srlz.data})
        else :
            return JsonResponse({'message':srlz.errors})

    
    if request.method == 'DELETE':
        rout.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    
