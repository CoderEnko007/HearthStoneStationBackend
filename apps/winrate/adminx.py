import xadmin
from .models import HSWinRate, DeckNameTranslate

class HSWinRateAdmin(object):
    list_display = ['faction', 'archetype', 'winrate', 'popularity', 'games', 'create_time']
    list_filter = ['faction', 'winrate', 'popularity', 'games', 'create_time']
    search_fields = ['faction', 'archetype']
    list_per_page = 15

class DeckNameTranslateAdmin(object):
    list_display = ['faction', 'ename', 'cname', 'create_time']
    list_filter = ['faction',]
    search_fields = ['faction', 'ename', 'cname']
    list_editable = ['cname',]
    list_per_page = 15

xadmin.site.register(HSWinRate, HSWinRateAdmin)
xadmin.site.register(DeckNameTranslate, DeckNameTranslateAdmin)