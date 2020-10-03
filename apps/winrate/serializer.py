from rest_framework import serializers
from .models import HSWinRate, DeckNameTranslate
from utils.globalVar import globalFunc

class ModifyHSWinRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSWinRate
        fields = "__all__"

class HSWinRateSerializer(serializers.ModelSerializer):
    faction = serializers.SerializerMethodField()
    create_time = serializers.SerializerMethodField()

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d')

    def get_faction(self, obj):
        FACTION_TYPE = {'Druid': '德鲁伊', 'Hunter': '猎人', 'Mage': '法师', 'Paladin': '圣骑士', 'Priest': '牧师', 'Rogue': '潜行者',
                        'Shaman': '萨满', 'Warlock': '术士', 'Warrior': '战士', 'DemonHunter': '恶魔猎手', 'Demonhunter': '恶魔猎手', 'Neutral': '中立'}
        faction = globalFunc.get_value(FACTION_TYPE, obj.faction)
        faction = faction[0] if len(faction)>0 else ''
        return dict({'id': obj.faction, 'faction': faction})

    class Meta:
        model = HSWinRate
        fields = "__all__"

class HSWinRateVisSerializer(serializers.ModelSerializer):
    faction = serializers.SerializerMethodField()

    def get_faction(self, obj):
        FACTION_TYPE = {'Druid': '德鲁伊', 'Hunter': '猎人', 'Mage': '法师', 'Paladin': '圣骑士', 'Priest': '牧师', 'Rogue': '潜行者',
                        'Shaman': '萨满', 'Warlock': '术士', 'Warrior': '战士', 'Demonhunter': '恶魔猎手', 'Neutral': '中立'}
        faction = globalFunc.get_value(FACTION_TYPE, obj.faction)
        faction = faction[0] if len(faction) > 0 else ''
        return dict({'id': obj.faction, 'faction': faction})

    class Meta:
        model = HSWinRate
        fields = "__all__"


class DeckNameTranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckNameTranslate
        fields = "__all__"