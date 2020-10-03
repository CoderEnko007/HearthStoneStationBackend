# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters
import datetime
import sys

from .models import Archetype


class ArchetypeFilter(filters.FilterSet):
    update_time = filters.DateTimeFilter(method='update_time_filter')

    def update_time_filter(self, queryset, name, value):
        # self.TraceStack()
        start_date = value
        end_date = value + datetime.timedelta(hours=23) + datetime.timedelta(minutes=59)
        return queryset.filter(update_time__range=(start_date, end_date))

    # @staticmethod
    # def TraceStack():
    #     print("--------------------")
    #     frame = sys._getframe(1)
    #     while frame:
    #         print(frame.f_code.co_name,)
    #         print(frame.f_code.co_filename,)
    #         print(frame.f_lineno)
    #         frame = frame.f_back
    class Meta:
        model = Archetype
        fields = ['faction', 'tier', 'rank_range', 'archetype_name', 'update_time']