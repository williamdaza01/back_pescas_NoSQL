from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from PescaNoSql.models import Cuenca, Pesca, Metodo
from PescaNoSql.serializers import MetodoSerializer, PescaSerializer, CuencaSerializer

# Create your views here.
@csrf_exempt
def metodoApi(request, cod=0):
    if request.method == 'GET':
        metodo = Metodo.objects.all()
        metodo_serializer = MetodoSerializer(metodo, many=True)
        return JsonResponse(metodo_serializer.data, safe=False)
    elif request.method == 'POST':
        metodo_data = JSONParser().parse(request)
        metodo_serializer = MetodoSerializer(data=metodo_data)
        print(metodo_serializer)
        if metodo_serializer.is_valid():
            metodo_serializer.save()
            return JsonResponse("Metodo agregado exitosamente", safe=False)
        return JsonResponse("Error al agregar metodo", safe=False)
    elif request.method == 'PUT':
        metodo_data = JSONParser().parse(request)
        metodo = Metodo.objects.get(ID_METODO=cod)
        metodo_serializer = MetodoSerializer(metodo,data=metodo_data)
        if metodo_serializer.is_valid():
            metodo_serializer.save()
            return JsonResponse("Metodo actualizado exitosamente", safe=False)
        return JsonResponse("Error al actualizar metodo", safe=False)
    elif request.method == 'DELETE':
        metodo = Metodo.objects.get(ID_METODO=cod)
        metodo.delete()
        return JsonResponse("Metodo eliminado exitosamente", safe=False)
    else:
        print("error")

@csrf_exempt
def cuencasApi(request, cod=0):
    if request.method == 'GET':
        cuenca = Cuenca.objects.all()
        cuenca_serializer = CuencaSerializer(cuenca, many=True)
        return JsonResponse(cuenca_serializer.data, safe=False)
    elif request.method == 'POST':
        cuenca_data = JSONParser().parse(request)
        cuenca_serializer = CuencaSerializer(data=cuenca_data)
        if cuenca_serializer.is_valid():
            cuenca_serializer.save()
            return JsonResponse("Cuenca agregada exitosamente", safe=False)
        return JsonResponse("Error al agregar cuenca", safe=False)
    elif request.method == 'PUT':
        cuenca_data = JSONParser().parse(request)
        cuenca = Cuenca.objects.get(ID_CUENCA=cod)
        cuenca_serializer = CuencaSerializer(cuenca,data=cuenca_data)
        if cuenca_serializer.is_valid():
            cuenca_serializer.save()
            return JsonResponse("Cuenca actualizada exitosamente", safe=False)
        return JsonResponse("Error al actualizar Cuenca", safe=False)
    elif request.method == 'DELETE':
        cuenca = Cuenca.objects.get(ID_CUENCA=cod)
        cuenca.delete()
        return JsonResponse("Cuenca eliminada exitosamente", safe=False)
    else:
        print("error")

@csrf_exempt
def pescasApi(request, cod=0):
    if request.method == 'GET':
        pescas = Pesca.objects.all()
        pescas_serializer = PescaSerializer(pescas, many=True)
        return JsonResponse(pescas_serializer.data, safe=False)
    elif request.method == 'POST':
        pescas_data = JSONParser().parse(request)
        pescas_serializer = PescaSerializer(data=pescas_data)
        if pescas_serializer.is_valid():
            pescas_serializer.save()
            return JsonResponse("Pesca agregada exitosamente", safe=False)
        return JsonResponse("Error al agregar pesca", safe=False)
    elif request.method == 'PUT':
        pescas_data = JSONParser().parse(request)
        pescas = Pesca.objects.get(ID_PESCA=cod)
        pescas_serializer = PescaSerializer(pescas,data=pescas_data)
        if pescas_serializer.is_valid():
            pescas_serializer.save()
            return JsonResponse("Pesca actualizada exitosamente", safe=False)
        return JsonResponse("Error al actualizar pesca", safe=False)
    elif request.method == 'DELETE':
        pescas = Pesca.objects.get(ID_PESCA=cod)
        pescas.delete()
        return JsonResponse("Pesca eliminada exitosamente", safe=False)
    else:
        print("error")