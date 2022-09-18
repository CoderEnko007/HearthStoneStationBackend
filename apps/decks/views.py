from django.shortcuts import render
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from cards.models import HSCards
from .models import Decks, Trending
from .serializer import DecksSerializer, TrendingSerializer
from .filters import DecksFilter, TrendingFilter
from utils.pyhearthstone import HearthStoneDeck
from hearthstone.enums import FormatType

import re
import json
from datetime import datetime
from dbtools.iFanr import iFanr


# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 10000


def upload_to_ifanr(data):
    if not data['deck_name']:
        return
    ifanr = iFanr()
    if data['mode'] == 'Wild':
        tableID = ifanr.tablesID['wild_decks']
    elif data['mode'] == 'Standard':
        tableID = ifanr.tablesID['standard_decks']
    else:
        tableID = ifanr.tablesID['classic_decks']
    query = {
        'where': json.dumps({
            'deck_id': {'$eq': data['deck_id']}
        }),
    }
    res = ifanr.get_table_data(tableID=tableID, query=query)
    if res:
        if res.get('meta').get('total_count'):
            deck = res.get('objects')[0]
            if not deck.get('game_count'):
                data['game_count'] = 400
            if data['last_30_days'] and not data['trending_flag']:
                data.pop('last_30_days')
                data.pop('win_rate')
                data.pop('game_count')
            print('last_30_days:', data['last_30_days'])
            ifanr.put_table_data(tableID=tableID, id=deck['id'], data=data)
        else:
            if not data.get('game_count'):
                data['game_count'] = 400
            ifanr.add_table_data(tableID=tableID, data=data)
    else:
        print('yf_log res is none')


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Decks.objects.all()
    pagination_class = PostPagination
    serializer_class = DecksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'deck_name')
    filter_class = DecksFilter
    ordering_fields = ('game_count', 'create_time')

    def create(self, request, *args, **kwargs):
        data = format_deck(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        data['card_array'] = json.loads(data['card_array'])
        data['set_array'] = json.loads(data['set_array'])
        upload_to_ifanr(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = format_deck(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data['card_array'] = json.loads(data['card_array'])
        data['set_array'] = json.loads(data['set_array'])
        upload_to_ifanr(data)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class TrendingViewSet(viewsets.ModelViewSet):
    queryset = Trending.objects.all()
    pagination_class = PostPagination
    serializer_class = TrendingSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'deck_name')
    filter_class = TrendingFilter
    ordering_fields = ('win_rate', 'game_count', 'create_time')

    def create(self, request, *args, **kwargs):
        data = format_deck(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = format_deck(request.data)
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


def format_deck(data):
    card_list = data.get('card_list', [])
    hsCards = []
    card_array = []
    set_array = []
    clazzCount = {'MINION': 0, 'SPELL': 0, 'WEAPON': 0, 'HERO': 0}  # 类别组成
    rarityCount = {'FREE': 0, 'COMMON': 0, 'RARE': 0, 'EPIC': 0, 'LEGENDARY': 0}  # 稀有统计
    statistic = [0] * 8  # 费用统计

    format_mode = FormatType.FT_STANDARD
    if data['mode'] == 'Wild':
        format_mode = FormatType.FT_WILD
    elif data['mode'] == 'Classic':
        format_mode = FormatType.FT_CLASSIC

    for card in card_list:
        print(card['card_hsid'])
        filter_card = HSCards.objects.get(hsId=card['card_hsid'])
        # 为card_array字段添加单卡的dbfId，用于根据单卡检索卡组
        card_array.append(filter_card.dbfId)
        if filter_card.set_id not in set_array:
            set_array.append(filter_card.set_id)
        # 用于生成卡组代码
        count = card.get('count')
        hsCards.append((filter_card.dbfId, count))
        # 套牌组成数据统计
        # 临时去除场地卡统计
        if filter_card.type != 'LOCATION':
            clazzCount[filter_card.type] += count
        rarityCount[filter_card.rarity] += count
        if filter_card.cost >= 7:
            statistic[7] += count
        else:
            statistic[filter_card.cost] += count
        card.update({'dbfId': filter_card.dbfId})
        card.update({'rarity': filter_card.rarity})
        card.update({'cname': filter_card.name})
        if filter_card.img_tile_link:
            tile = re.match('^.*\/(.*\.png)', filter_card.img_tile_link)
            tile = tile.group(1) if tile is not None else ''
            card.update({'tile': tile})
        else:
            card.update({'tile': ''})
    try:
        hsDeck = HearthStoneDeck(hero=data['faction'], cards=hsCards, format=format_mode)
        deck_code = hsDeck.genDeckString()
    except Exception as e:
        deck_code = ''
        print('generate deck code error', e, data['deck_id'], card_list)
    data['deck_code'] = deck_code
    data['card_list'] = json.dumps(data.get('card_list', '[]'), ensure_ascii=False)
    data['mulligan'] = json.dumps(data.get('mulligan', '[]'), ensure_ascii=False)
    data['clazzCount'] = json.dumps(clazzCount, ensure_ascii=False)
    data['rarityCount'] = json.dumps(rarityCount, ensure_ascii=False)
    data['statistic'] = json.dumps(statistic, ensure_ascii=False)
    data['card_array'] = json.dumps(card_array, ensure_ascii=False)
    data['set_array'] = json.dumps(set_array, ensure_ascii=False)
    data['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data
