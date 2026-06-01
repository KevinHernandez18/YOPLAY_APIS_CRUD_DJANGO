# from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import TutorialesViewSet

# from django.contrib import admin
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = DefaultRouter()

# registro de endpoints del api 

router.register(r'tutoriales', TutorialesViewSet, basename='tutoriales')

urlpatterns = router.urls