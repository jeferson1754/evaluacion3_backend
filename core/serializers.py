from rest_framework import serializers
from .models import *

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        depth =1
        
        
class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = '__all__'
        depth =1