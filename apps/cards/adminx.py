import xadmin
from .models import Cards, Series


class CardsAdmin(object):
    list_display = ["cname", "ename", "description", "faction", "clazz", \
                   "race", "rarity", "rule", "series", "mode"]
    list_filter = ["mana", "hp", "cname", "faction", "clazz", "race", "rarity", "series", "mode"]
    search_fields = ['cname', 'ename']
    readonly_fields = ('image_img','image_thumb')
    exclude = ['img', 'thumbnail']  # 排除该字段
    ordering = ('mana',)
    list_per_page = 10

class SeriesAdmin(object):
    list_display = ["cname", "ename", "create_time"]

xadmin.site.register(Series, SeriesAdmin)
xadmin.site.register(Cards, CardsAdmin)