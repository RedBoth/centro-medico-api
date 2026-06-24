from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Especialidad, Medico, Turno
from .serializers import EspecialidadSerializer, MedicoSerializer, TurnoCreateSerializer, TurnoDetalleSerializer
from django.shortcuts import get_object_or_404

class EspecialidadListAPIView(APIView):
  def get(self, request):
    especialidades = Especialidad.objects.all()
    serializer = EspecialidadSerializer(especialidades, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class MedicoListAPIView(APIView):
  def get(self, request):
    medicos = Medico.objects.select_related('usuario', 'especialidad').all()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class TurnoListCreateAPIView(APIView):
  def get(self, request):
    queryset = Turno.objects.select_related('paciente', 'medico__usuario', 'medico__especialidad').all()

    estado_filtro = request.query_params.get('estado')
    medico_filtro = request.query_params.get('medico_id')

    if estado_filtro is not None:
      queryset = queryset.filter(estado=estado_filtro)

    if medico_filtro is not None:
      queryset = queryset.filter(medico_id=medico_filtro)

    queryset = queryset.order_by('-fecha_hora')

    serializer = TurnoDetalleSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = TurnoCreateSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      response_serializer = TurnoDetalleSerializer(serializer.instance)
      return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TurnoDetailAPIView(APIView):
  def get_object(self, pk):
    return get_object_or_404(Turno, pk=pk)
  
  # 1. GET /api/turnos/<id>/ -> Ver un solo turno con todo el detalle amigable
  def get(self, request, pk):
    turno = self.get_object(pk)
    serializer = TurnoDetalleSerializer(turno);
    return Response(serializer.data, status=status.HTTP_200_OK)

  def patch(self, request, pk):
    turno = self.get_object(pk)
    serializer = TurnoCreateSerializer(turno, data=request.data, partial=True)

    if serializer.is_valid():
      serializer.save()
      response_serializer = TurnoDetalleSerializer(turno)
      return Response(response_serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
