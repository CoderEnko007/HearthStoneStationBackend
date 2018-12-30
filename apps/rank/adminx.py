import xadmin
from .models import HSRanking

class HSRankingAdmin(object):
    list_display = ['game_type', 'faction', 'win_rate', 'report_time']
    list_filter = ['game_type', 'report_time', 'faction']
    search_fields = ['game_type', 'faction']
    ordering = ('-win_rate',)

xadmin.site.register(HSRanking, HSRankingAdmin)