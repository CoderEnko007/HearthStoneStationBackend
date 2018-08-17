from rest_framework import serializers
from .models import Cards, Series
from utils.globalVar import globalFunc


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("cname", "ename", "image")

class CardsSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    clazz = serializers.SerializerMethodField()
    rarity = serializers.SerializerMethodField()
    faction = serializers.SerializerMethodField()

    def get_clazz(self, obj):
        CLAZZ_TYPE = {'1': '随从', '2': '法术', '3': '装备', '4': '英雄牌'}
        clazz = globalFunc.get_value(CLAZZ_TYPE, obj.clazz)[0]
        return dict({'id': obj.clazz, 'name': clazz})

    def get_rarity(self, obj):
        RARITY_TYPE = {'1': '基本', '2': '普通', '3': '稀有', '4': '史诗', '5': '传说'}
        rarity = globalFunc.get_value(RARITY_TYPE, obj.rarity)[0]
        return dict({'id': obj.rarity, 'name': rarity})

    def get_faction(self, obj):
        FACTION_TYPE = {'Druid': '德鲁伊', 'Hunter': '猎人', 'Mage': '法师', 'Paladin': '圣骑士', 'Priest':
            '牧师', 'Rogue': '潜行者', 'Shaman': '萨满', 'Warlock': '术士', 'Warrior': '战士', 'Neutral': '中立'}
        faction = globalFunc.get_value(FACTION_TYPE, obj.faction)[0]
        return dict({'id': obj.faction, 'name': faction})

    class Meta:
        model = Cards
        fields = "__all__"