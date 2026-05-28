from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DocumentoViewSet,
    UsuarioViewSet,
    ContrasenaViewSet,
    HistorialAccesoViewSet
)
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

# registro de los endpoints del api

router.register(r'documento', DocumentoViewSet)
router.register(r"usuario",UsuarioViewSet)
router.register(r'contrasena',ContrasenaViewSet)
router.register(r'historial_acceso',HistorialAccesoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]