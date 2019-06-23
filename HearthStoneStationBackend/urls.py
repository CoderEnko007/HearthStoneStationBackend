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
from cards.views import CardsViewSet, HSCardsViewSet, ArenaCardsViewSet
from rank.views import HSRankingViewSet
from winrate.views import HSWinRateViewSet, DeckNameTranslateViewSet
from decks.views import DecksViewSet, TrendingViewSet
from archetype.views import ArchetypeSet
from wechat.views import WeChat

from werobot.contrib.django import make_view
from wechat.robot import robot

router = DefaultRouter()
# router.register(r'cards', CardsViewSet, base_name='cards')
router.register(r'rank', HSRankingViewSet, base_name='rank')
router.register(r'rank-vis', HSRankingViewSet, base_name='rank-vis')
router.register(r'winrate', HSWinRateViewSet, base_name='winrate')
router.register(r'winrate-vis', HSWinRateViewSet, base_name='winrate-vis')
router.register(r'decks', DecksViewSet, base_name='decks')
router.register(r'trending', TrendingViewSet, base_name='trending')
router.register(r'cards', HSCardsViewSet, base_name='cards')
router.register(r'arenaCards', ArenaCardsViewSet, base_name='arenaCards')
router.register(r'archetype', ArchetypeSet, base_name='archetype')
router.register(r'archetype-vis', ArchetypeSet, base_name='archetype-vis')
router.register(r'deckname', DeckNameTranslateViewSet, base_name='deckname')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('media/<path:path>/', serve, {'document_root': MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='炉石传说情报站管理系统')),

    path('wechat', WeChat.as_view()),
    path('robot', make_view(robot)),
    # path('wechat/', include('wechat.urls')),

    path('', include(router.urls)),
]
