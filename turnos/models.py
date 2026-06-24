from django.db import models
from django.contrib.auth.models import User

class Especialidad(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  descripcion = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.nombre
  
class Medico(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name="medicos")
  matricula = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return f"Dr. {self.usuario.last_name}, {self.usuario.first_name} {self.especialidad.nombre}"
  
class Turno(models.Model):
  STATUS_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('confirmado', 'Confirmado'),
    ('atendido', 'Atendido'),
    ('cancelado', 'Cancelado'),
  ]

  paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="turnos_paciente")
  medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="turnos_medico")

  fecha_hora = models.DateTimeField()
  motivo_consulta = models.TextField(blank=True, null=True)
  estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
  creado_en = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Turno: {self.paciente.username} con {self.medico} - {self.fecha_hora}"