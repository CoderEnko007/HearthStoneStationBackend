# -*- coding: utf-8 -*-
import django_filters
from django_filters.rest_framework import FilterSet

from .models import Cards


class CardsFilter(FilterSet):
    # cname = filters.CharFilter(name="cname", lookup_expr='icontains', label='卡牌名称')
    cname = django_filters.CharFilter(name='cname', lookup_expr='icontains', label='卡牌名称')
    # seriesName = filters.CharFilter(name="seriesName", lookup_expr='iexact', label='卡牌系列')
    # mode = filters.CharFilter(name="mode", lookup_expr='iexact', label='赛制')
    # faction = filters.CharFilter(name='faction', lookup_expr='iexact', label='职业')

    class Meta:
        model = Cards
        fields = ['cname',]