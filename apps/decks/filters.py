# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
import datetime

from .models import Decks, Trending


class DecksFilter(filters.FilterSet):
    create_time = filters.DateTimeFilter(method='create_time_filter')

    def create_time_filter(self, queryset, name, value):
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(create_time__range=(start_date, end_date))

    class Meta:
        model = Decks
        fields = ['faction', 'deck_id', 'deck_name', 'create_time']


class TrendingFilter(filters.FilterSet):
    create_time = filters.DateTimeFilter(method='create_time_filter')

    def create_time_filter(self, queryset, name, value):
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(create_time__range=(start_date, end_date))

    class Meta:
        model = Trending
        fields = ['faction', 'deck_id', 'deck_name', 'create_time']