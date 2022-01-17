from django.shortcuts import render
from .models import HSRanking
from .serializer import HSRankingSerializer, HSRankingVisSerializer
from .filters import RankFilter

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class RankingPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 3000

class HSRankingViewSet(viewsets.ModelViewSet):
    queryset = HSRanking.objects.all()
    pagination_class = RankingPagination
    # serializer_class = HSRankingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('mode', 'report_time')
    filter_class = RankFilter
    ordering_fields = ('report_time', )

    def get_serializer_class(self):
        if self.basename == 'rank-vis':
            return HSRankingVisSerializer
        elif self.basename == 'rank':
            return HSRankingSerializer
        else:
            return HSRankingVisSerializer
