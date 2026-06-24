from rest_framework import serializers
from .models import Especialidad, Medico, Turno
from django.contrib.auth.models import User
from django.utils import timezone

# Serializadores de lectura

class EspecialidadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Especialidad
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email']

class MedicoSerializer(serializers.ModelSerializer):
  usuario = UserSerializer(read_only=True)
  especialidad_nombre = serializers.ReadOnlyField(source='especialidad.nombre')

  class Meta:
    model = Medico
    fields = ['id', 'usuario', 'especialidad_nombre', 'matricula']

class TurnoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Turno
    fields = ['id', 'paciente', 'medico', 'fecha_hora', 'motivo_consulta', 'estado']

  def validate(self, data):
    fecha_hora = data.get('fecha_hora')
    medico = data.get('medico')

    if fecha_hora is not None:
      if(fecha_hora < timezone.now()):
        raise serializers.ValidationError({"fecha_hora":"No puedes agendar un turno en una fecha u hora pasada."})
    
    current_medico = medico if medico is not None else getattr(self.instance, 'medico', None)
    current_fecha = fecha_hora if fecha_hora is not None else getattr(self.instance, 'fecha_hora', None)
    if current_medico and current_fecha and (fecha_hora is not None or medico is not None):
      query = Turno.objects.filter(medico=current_medico, fecha_hora=current_fecha).exclude(estado='cancelado')
      
      if self.instance:
        query = query.exclude(pk=self.instance.pk)

      if query.exists():
        raise serializers.ValidationError({"fecha_hora": "El medico ya tiene un turno asignado para esta fecha y hora."})

    return data;

class TurnoDetalleSerializer(serializers.ModelSerializer):
  paciente = UserSerializer(read_only=True)
  medico = MedicoSerializer(read_only=True)

  class Meta:
    model = Turno
    fields = ['id', 'paciente', 'medico', 'fecha_hora', 'motivo_consulta', 'estado', 'creado_en']