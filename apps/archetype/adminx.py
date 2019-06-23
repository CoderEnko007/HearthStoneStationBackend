import xadmin
from .models import Archetype

class ArchetypeAdmin(object):
    list_display = ['archetype_name', 'rank_range', 'tier', 'faction', 'win_rate', 'game_count', 'popularity', 'update_time']
    list_filter = ['tier', 'rank_range', 'faction', 'archetype_name', 'update_time']
    search_fields = ['archetype_name', ]
    ordering = ('tier', 'win_rate')
    list_per_page = 10

xadmin.site.register(Archetype, ArchetypeAdmin)

