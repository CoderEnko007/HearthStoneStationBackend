from rest_framework import serializers
from .models import Archetype

class ArchetypeSerializer(serializers.ModelSerializer):
    update_time = serializers.SerializerMethodField()

    def get_update_time(self, obj):
        return obj.update_time.strftime('%Y-%m-%d')
    class Meta:
        model = Archetype
        fields = "__all__"