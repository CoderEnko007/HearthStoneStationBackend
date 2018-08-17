from django.shortcuts import render

from .serializer import CardsSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Cards
from .filters import CardsFilter

# Create your views here.
class CardsPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = page_size
    page_query_param = 'page'
    max_page_size = 3000


class CardsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    卡牌列表
    """
    queryset = Cards.objects.all().order_by('mana')
    serializer_class = CardsSerializer
    pagination_class = CardsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CardsFilter
    # filter_fields = ('cname', 'series', 'mode', 'faction', 'rarity', 'mana')
    search_fields = ('cname', 'faction', 'clazz', 'race', 'rarity', 'rule', 'series', 'mode')
    ordering_fields = ('mana', )