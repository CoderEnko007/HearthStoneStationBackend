from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Archetype
from .serializer import ArchetypeSerializer
from .filters import ArchetypeFilter

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = page_size
    page_query_param = 'page'
    max_page_size = 10000

class ArchetypeSet(viewsets.ReadOnlyModelViewSet):
    queryset = Archetype.objects.all()
    pagination_class = PostPagination
    serializer_class = ArchetypeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('faction', 'tier')
    filter_class = ArchetypeFilter
    search_fields = ('archetype_name', )
    ordering_fields = ('game_count', 'update_time')
