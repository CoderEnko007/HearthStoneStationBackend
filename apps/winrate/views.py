from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import HSWinRate, DeckNameTranslate
from .serializer import HSWinRateSerializer, HSWinRateVisSerializer, DeckNameTranslateSerializer, ModifyHSWinRateSerializer
from .filters import WinRateFilter
from utils.pyhearthstone import HearthStoneDeck
from cards.models import HSCards
from datetime import datetime

import json
import re
# Create your views here.


class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 10000


class HSWinRateViewSet(viewsets.ModelViewSet):
    queryset = HSWinRate.objects.all()
    pagination_class = PostPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'create_time')
    filter_class = WinRateFilter
    ordering_fields = ('create_time', )

    def create(self, request, *args, **kwargs):
        data = format_data(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = format_data(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'create':
            return ModifyHSWinRateSerializer
        else:
            if self.basename == 'winrate-vis':
                return HSWinRateVisSerializer
            elif self.basename == 'winrate':
                return HSWinRateSerializer
            else:
                return HSWinRateVisSerializer


class DeckNameTranslateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeckNameTranslate.objects.all()
    pagination_class = PostPagination
    serializer_class = DeckNameTranslateSerializer


def format_cards_list(cards_list):
    for cards in cards_list:
        for card in cards:
            res_card = HSCards.objects.get(hsId=card['card_hsid'])
            card.update({'dbfId': res_card.dbfId})
            card.update({'rarity': res_card.rarity})
            card.update({'cname': res_card.name})
            if res_card.img_tile_link:
                tile = re.match('^.*\/(.*\.png)', res_card.img_tile_link)
                tile = tile.group(1) if tile is not None else ''
                card.update({'tile': tile})
            else:
                card.update({'tile': ''})
    return cards_list

def format_data(data):
    if data['archetype'] != 'Other' and data['rank_range'] == 'BRONZE_THROUGH_GOLD':
        core_cards = data['core_cards']
        pop_cards = data['pop_cards']
        format_list = format_cards_list([core_cards, pop_cards])
        data['core_cards'] = json.dumps(format_list[0], ensure_ascii=False)
        data['pop_cards'] = json.dumps(format_list[1], ensure_ascii=False)
    data['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

