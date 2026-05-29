from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    encuentroViewSet,
    grupoViewSet,
    grupo_encuentroViewSet,
    grupo_equipoViewSet
)

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

# Registro de endpoints del API.

router.register(r'encuentros', encuentroViewSet)
router.register(r'grupos', grupoViewSet)
router.register(r'grupo_encuentros', grupo_encuentroViewSet)
router.register(r'grupo_equipos', grupo_equipoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]