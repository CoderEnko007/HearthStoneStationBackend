from django.shortcuts import render

from .serializer import CardsSerializer, HSCardsSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Cards, HSCards
from .filters import CardsFilter, HSCardsFilter

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


class HSCardsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HSCards.objects.all().order_by('cost')
    serializer_class = HSCardsSerializer
    pagination_class = CardsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = HSCardsFilter
    # filter_fields = ('cname', 'series', 'mode', 'faction', 'rarity', 'mana')
    search_fields = ('name', 'cardClass', 'type', 'race', 'rarity', 'mechanics', 'set', 'artist')
    ordering_fields = ('cost',)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        import copy
        assert self.paginator is not None
        for index, item in enumerate(data):
            temp = copy.deepcopy(item)
            for key, value in temp.items():
                if value is None:
                    item.pop(key)
        return self.paginator.get_paginated_response(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer_data = serializer.data
        import copy
        temp = copy.deepcopy(serializer_data)
        for key, value in temp.items():
            if value is None:
                del serializer_data[key]
        return Response(serializer_data)