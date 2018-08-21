import xadmin
from .models import Decks

class DecksAdmin(object):
    list_display = ['deck_name', 'faction', 'dust_cost', 'win_rate', 'game_count', 'duration']
    list_filter = ['deck_name', 'faction', 'win_rate', 'game_count']
    search_fields = ['deck_name', 'faction']
    ordering = ('-game_count',)
    list_per_page = 30

xadmin.site.register(Decks, DecksAdmin)

    