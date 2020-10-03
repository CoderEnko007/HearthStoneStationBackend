from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Battlegrounds
from .serializer import BattlegroundsSerializer
from .filters import BattlegroundsFilter

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 10000

class BattlegroundsSet(viewsets.ReadOnlyModelViewSet):
    queryset = Battlegrounds.objects.all()
    pagination_class = PostPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'tier')
    filter_class = BattlegroundsFilter
    search_fields = ('hero',)
    ordering_fields = ('tier', 'avg_final_placement')

    def get_serializer_class(self):
        return BattlegroundsSerializer