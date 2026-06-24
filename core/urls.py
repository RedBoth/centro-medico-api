"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from turnos.views import EspecialidadListAPIView, MedicoListAPIView, TurnoListCreateAPIView, TurnoDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/especialidades/', EspecialidadListAPIView.as_view(), name='api-especialidades'),
    path('api/medicos/', MedicoListAPIView.as_view(), name='api-medicos'),
    path('api/turnos/', TurnoListCreateAPIView.as_view(), name='api-turnos'),
    path('api/turnos/<int:pk>/', TurnoDetailAPIView.as_view(), name='api-turno-detalle')
]
