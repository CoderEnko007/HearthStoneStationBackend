from rest_framework import serializers
from .models import Cards, Series


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("cname", "ename", "image")

class CardsSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    class Meta:
        model = Cards
        fields = "__all__"