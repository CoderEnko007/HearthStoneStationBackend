# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
import datetime

from .models import Battlegrounds


class BattlegroundsFilter(filters.FilterSet):
    update_time = filters.DateTimeFilter(method='update_time_filter')

    def update_time_filter(self, queryset, name, value):
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(update_time__range=(start_date, end_date))

    class Meta:
        model = Battlegrounds
        fields = ['tier', 'hero', 'mmr_range', 'time_frame', 'update_time']