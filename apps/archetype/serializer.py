from rest_framework import serializers
from .models import Archetype

class ArchetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = "__all__"