from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Routine,RoutineSerializers,classes,classesSerializers


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def classstate(request):
    state=get_object_or_404(classes,id=1)
    if request.method == 'GET':
        serializer=classesSerializers(state)
        return JsonResponse(serializer.data)
    
    if request.method == 'POST':
        serializer=classesSerializers(state,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'message':serializer.errors})
        


 
@api_view(['GET','POST'])
def routine(request):
    if request.method == 'GET':
        rout=Routine.objects.all()
        serializer=RoutineSerializers(rout,many=True)
        return JsonResponse({'Routine :': serializer.data})

    if request.method == 'POST':
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
    
@api_view(['GET'])
def routine_sec(request,sec):
    sec=sec.upper()
    try:
        rout = Routine.objects.filter(section=sec)
    except Routine.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        srlz=RoutineSerializers(rout,many=True)
        return JsonResponse({f'Routine/{sec}':srlz.data})
    

@api_view(['GET'])
def routine_sec_day(request,sec,day):
    sec=sec.upper()
    day=day.upper()
    try:
        rout = Routine.objects.filter(section=sec,weekday=day)
    except Routine.DoesNotExist:
        return JsonResponse(status=404)
    if request.method == 'GET':
        srlz=RoutineSerializers(rout,many=True)
        return JsonResponse({f'Routine/':srlz.data})
    