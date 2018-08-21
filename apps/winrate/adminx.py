import xadmin
from .models import HSWinRate

class HSWinRateAdmin(object):
    list_display = ['faction', 'archetype', 'winrate', 'popularity', 'games', 'create_time']
    list_filter = ['faction', 'winrate', 'popularity', 'games', 'create_time']
    search_fields = ['faction', 'archetype']
    list_per_page = 30

xadmin.site.register(HSWinRate, HSWinRateAdmin)