from rest_framework import serializers
from .models import Battlegrounds, HSBattleGroundCards

class HSBattleGroundCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSBattleGroundCards
        fields = "__all__"

class BattlegroundsSerializer(serializers.ModelSerializer):

    update_time = serializers.SerializerMethodField()
    hero = serializers.SerializerMethodField()
    final_placement_distribution = serializers.SerializerMethodField()

    def get_update_time(self, obj):
        return obj.update_time.strftime('%Y-%m-%d')

    def get_hero(self, obj):
        return {
            'hsId': int(obj.hero.hsId),
            'name': obj.hero.name,
            'ename': obj.hero.ename,
            'image': obj.hero.image
        }

    def get_final_placement_distribution(self, obj):
        return eval(obj.final_placement_distribution)

    class Meta:
        model = Battlegrounds
        fields = '__all__'