"""HearthStoneStationBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from HearthStoneStationBackend.settings import MEDIA_ROOT
from cards.views import CardsViewSet
from rank.views import HSRankingViewSet
from winrate.views import HSWinRateViewSet
from decks.views import DecksViewSet

router = DefaultRouter()
router.register(r'cards', CardsViewSet, base_name='cards')
router.register(r'rank', HSRankingViewSet, base_name='rank')
router.register(r'winrate', HSWinRateViewSet, base_name='winrate')
router.register(r'decks', DecksViewSet, base_name='decks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('media/<path:path>/', serve, {'document_root': MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='炉石传说情报站管理系统')),

    path('', include(router.urls)),
]
