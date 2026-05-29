from django.shortcuts import render

from rest_framework import viewsets

from .models import Tutoriales

from .serializers import TutorialesSerializer

# crud de tutoriales

class TutorialesViewSet(viewsets.ModelViewSet):
    queryset = Tutoriales.objects.all()
    serializer_class = TutorialesSerializer
