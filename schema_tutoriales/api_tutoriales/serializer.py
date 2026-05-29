from rest_framework import serializers
from .models import (tutoriales)

class TutorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tutoriales
        fields = '__all__'