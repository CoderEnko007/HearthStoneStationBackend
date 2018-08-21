from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import HSWinRate
from .serializer import HSWinRateSerializer

# Create your views here.

class HSWinRateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HSWinRate.objects.all()
    serializer_class = HSWinRateSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('faction', 'create_time')
    ordering_fields = ('create_time', )