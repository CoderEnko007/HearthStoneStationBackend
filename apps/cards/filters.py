# -*- coding: utf-8 -*-
# import django_filters
from django_filters import rest_framework as filters

from .models import Cards, HSCards, ArenaCards


class CardsFilter(filters.FilterSet):
    cname = filters.CharFilter(field_name='cname', lookup_expr='icontains', label='卡牌名称')
    min_mana = filters.NumberFilter(field_name='mana', lookup_expr='gte')

    class Meta:
        model = Cards
        fields = ['cname', 'mode', 'faction', 'rarity', 'clazz', 'series', 'min_mana']

class HSCardsFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='卡牌名称')
    min_cost = filters.NumberFilter(field_name='cost', lookup_expr='gte')

    class Meta:
        model = HSCards
        fields = ['name', 'cardClass', 'rarity', 'type', 'set', 'min_cost']

class HSArenaCardsFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='卡牌名称')
    min_cost = filters.NumberFilter(field_name='cost', lookup_expr='gte', label='最低费用')
    min_played = filters.NumberFilter(field_name='times_played', lookup_expr='gte', label='最少打出次数')

    class Meta:
        model = ArenaCards
        fields = ['name', 'cardClass', 'rarity', 'type', 'set', 'classification', 'min_cost', 'min_played', 'extra_data', 'update_time']