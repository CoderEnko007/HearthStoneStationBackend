from datetime import datetime
from rest_framework import serializers
from .models import HSRanking
from utils.globalVar import globalFunc


class HSRankingSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    report_time = serializers.SerializerMethodField()

    def get_report_time(self, obj):
        return obj.report_time.strftime('%Y-%m-%d')

    def get_name(self, obj):
        FACTION_TYPE = {'Druid': '德鲁伊', 'Hunter': '猎人', 'Mage': '法师', 'Paladin': '圣骑士', 'Priest':
            '牧师', 'Rogue': '潜行者', 'Shaman': '萨满', 'Warlock': '术士', 'Warrior': '战士', 'Neutral': '中立'}
        faction = globalFunc.get_value(FACTION_TYPE, obj.name)[0]
        return dict({'id': obj.name, 'name': faction})

    class Meta:
        model = HSRanking
        fields = "__all__"
