import xadmin
from .models import HSRanking

class HSRankingAdmin(object):
    list_display = ['mode', 'rank_no', 'name', 'winrate', 'report_time']
    list_filter = ['mode', 'report_time', 'rank_no', 'name']
    search_fields = ['mode', 'name']
    ordering = ('rank_no',)

xadmin.site.register(HSRanking, HSRankingAdmin)