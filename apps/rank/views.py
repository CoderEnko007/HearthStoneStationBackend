from django.shortcuts import render
from .models import HSRanking
from .serializer import HSRankingSerializer
from .filters import RankFilter

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class HSRankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HSRanking.objects.all()
    serializer_class = HSRankingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('mode', 'report_time')
    filter_class = RankFilter
    ordering_fields = ('report_time', )
