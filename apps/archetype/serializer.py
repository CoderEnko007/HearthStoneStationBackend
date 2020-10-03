from rest_framework import serializers
from .models import Archetype

class ModifyArchetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = "__all__"

class ArchetypeSerializer(serializers.ModelSerializer):
    update_time = serializers.SerializerMethodField()

    def get_update_time(self, obj):
        return obj.update_time.strftime('%Y-%m-%d')
    class Meta:
        model = Archetype
        fields = "__all__"

class ArchetypeVisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = "__all__"