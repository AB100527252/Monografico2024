from rest_framework import serializers
from .models import Partido


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Partido
        fields = ('nombre', 'ideologia', 'color')
        
        fields = '__all__'