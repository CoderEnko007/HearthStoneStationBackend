# -*- coding: utf-8 -*-
# import django_filters
from django_filters import rest_framework as filters

from .models import HSRanking


class RankFilter(filters.FilterSet):
    report_time = filters.DateFromToRangeFilter()
    rank_no = filters.NumberFilter(min_value=1, max_value=9)

    class Meta:
        model = HSRanking
        fields = ['mode', 'name', 'rank_no', 'report_time']