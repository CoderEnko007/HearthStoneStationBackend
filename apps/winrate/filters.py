# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
import datetime

from .models import HSWinRate


class WinRateFilter(filters.FilterSet):
    create_time = filters.DateTimeFilter(method='create_time_filter')

    def create_time_filter(self, queryset, name, value):
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(create_time__range=(start_date, end_date))

    class Meta:
        model = HSWinRate
        fields = ['faction', 'create_time']