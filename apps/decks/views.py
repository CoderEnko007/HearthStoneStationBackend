from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Decks
from .serializer import DecksSerializer
from .filters import DecksFilter

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    page_query_param = 'page'
    max_page_size = 10000

class DecksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Decks.objects.all()
    pagination_class = PostPagination
    serializer_class = DecksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'deck_name')
    filter_class = DecksFilter
    ordering_fields = ('game_count', 'create_time')
