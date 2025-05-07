from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Habitacion, Cliente, Reserva, Resena
from .serializers import *

from django.db.models import Q

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

@api_view(['GET'])
def verificar_disponibilidad(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    reservas_ocupadas = Reserva.objects.filter(
        Q(fecha_entrada__lt=fecha_fin) & Q(fecha_salida__gt=fecha_inicio),
        estado='activa'
    ).values_list('habitacion_id', flat=True)
    
    disponibles = Habitacion.objects.exclude(id__in=reservas_ocupadas)
    serializer = HabitacionSerializer(disponibles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_resena(request):
    serializer = ResenaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
