from django.shortcuts import render

from rest_framework import viewsets

from .models import Documento, Usuario, Contrasena, HistorialAcceso

from .serializers import DocumentoSerializer, UsuarioSerializer, ContrasenaSerializer, HistorialAccesoSerializer

# crud de documento 

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    
# crud de usuario
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
# crud de contrasena
    
class ContrasenaViewSet(viewsets.ModelViewSet):
    queryset = Contrasena.objects.all()
    serializer_class = ContrasenaSerializer
    
# crud de historial_acceso
    
class HistorialAccesoViewSet(viewsets.ModelViewSet):
    queryset = HistorialAcceso.objects.all()
    serializer_class = HistorialAccesoSerializer