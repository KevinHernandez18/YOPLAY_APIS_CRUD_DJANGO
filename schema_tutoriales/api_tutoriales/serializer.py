from rest_framework import serializers
from .models import Tutoriales

class TutorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoriales
        fields = '__all__'