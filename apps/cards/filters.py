# -*- coding: utf-8 -*-
# import django_filters
from django_filters import rest_framework as filters

from .models import Cards


class CardsFilter(filters.FilterSet):
    cname = filters.CharFilter(field_name='cname', lookup_expr='icontains', label='卡牌名称')
    min_mana = filters.NumberFilter(field_name='mana', lookup_expr='gte')

    class Meta:
        model = Cards
        fields = ['cname', 'mode', 'faction', 'rarity', 'clazz', 'series', 'min_mana']