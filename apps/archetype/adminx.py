import xadmin
from .models import Archetype

class ArchetypeAdmin(object):
    list_display = ['archetype_name', 'tier', 'faction', 'win_rate', 'game_count', 'popularity', 'update_time']
    list_filter = ['tier', 'faction', 'update_time']
    search_fields = ['archetype_name', ]
    ordering = ('tier', )

xadmin.site.register(Archetype, ArchetypeAdmin)

