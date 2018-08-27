from rest_framework import serializers
from .models import Decks

class DecksSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d')

    class Meta:
        model = Decks
        fields = "__all__"