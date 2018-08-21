from rest_framework import serializers
from .models import Decks

class DecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decks
        fields = "__all__"