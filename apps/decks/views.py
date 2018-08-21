from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Decks
from .serializer import DecksSerializer

# Create your views here.
class DecksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Decks.objects.all()
    serializer_class = DecksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('faction', 'deck_name')
    ordering_fields = ('-game_count',)
