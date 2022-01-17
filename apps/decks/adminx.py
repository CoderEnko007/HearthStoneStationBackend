import xadmin
from .models import Decks, Trending

class DecksAdmin(object):
    list_display = ['deck_name', 'faction', 'dust_cost', 'win_rate', 'game_count', 'duration', 'update_time']
    list_filter = ['deck_id', 'deck_name', 'faction', 'win_rate', 'game_count', 'mode', 'last_30_days', 'create_time', 'update_time']
    search_fields = ['deck_name', 'faction']
    ordering = ('-game_count',)
    list_per_page = 10

class TrendingAdmin(object):
    list_display = ['deck_name', 'faction', 'dust_cost', 'win_rate', 'game_count', 'duration', 'update_time']
    list_filter = ['deck_id', 'deck_name', 'faction', 'win_rate', 'game_count', 'create_time', 'update_time']
    search_fields = ['deck_name', 'faction']
    ordering = ('-win_rate',)
    list_per_page = 10

xadmin.site.register(Decks, DecksAdmin)
xadmin.site.register(Trending, TrendingAdmin)

    