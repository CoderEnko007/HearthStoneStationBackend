# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
import datetime

from .models import HSRanking


class RankFilter(filters.FilterSet):
    report_time = filters.DateTimeFilter(method='report_time_filter')

    def report_time_filter(self, queryset, name, value):
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(report_time__range=(start_date, end_date))

    class Meta:
        model = HSRanking
        fields = ['game_type', 'faction', 'report_time']