from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import HSWinRate, DeckNameTranslate
from .serializer import HSWinRateSerializer, DeckNameTranslateSerializer
from .filters import WinRateFilter

# Create your views here.

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    page_query_param = 'page'
    max_page_size = 10000

class HSWinRateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HSWinRate.objects.all()
    pagination_class = PostPagination
    serializer_class = HSWinRateSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'create_time')
    filter_class = WinRateFilter
    ordering_fields = ('create_time', )


class DeckNameTranslateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeckNameTranslate.objects.all()
    pagination_class = PostPagination
    serializer_class = DeckNameTranslateSerializer