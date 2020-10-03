import xadmin
from .models import Battlegrounds

class BattlegroundsAdmin(object):
    list_display = ['hero', 'mmr_range', 'time_frame', 'tier', 'avg_final_placement', 'pick_rate', 'times_offered', 'times_chosen', 'update_time']
    list_filter = ['tier', 'mmr_range', 'time_frame', 'update_time']
    search_fields = ['hero__name', 'hero__id']
    ordering = ('tier', 'avg_final_placement')
    list_per_page = 10

xadmin.site.register(Battlegrounds, BattlegroundsAdmin)

