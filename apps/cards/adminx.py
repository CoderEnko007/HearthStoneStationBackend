import xadmin
from .models import Cards, Series, HSCards, ArenaCards


class CardsAdmin(object):
    list_display = ["cname", "ename", "description", "faction", "clazz", \
                   "race", "rarity", "rule", "series", "mode"]
    list_filter = ["mana", "hp", "cname", "faction", "clazz", "race", "rarity", "series", "mode"]
    search_fields = ['cname', 'ename']
    readonly_fields = ('image_img','image_thumb')
    exclude = ['img', 'thumbnail']  # 排除该字段
    ordering = ('mana',)
    list_per_page = 10

class HSCardsAdmin(object):
    list_display = ['hsId', 'name', 'ename', 'cardClass', 'set', 'artist', 'invalid', 'image_img', 'entourage']
    list_filter = ['dbfId', 'cost', 'health', 'cardClass', 'rarity', 'type', 'race', 'set', 'collectible', 'invalid']
    search_fields = ['hsId', 'name', 'ename']
    readonly_fields = ('image_img', 'image_thumb')
    ordering = ('cost',)
    list_editable = ["invalid", ]
    list_per_page = 10

class ArenaCardsAdmin(object):
    list_display = ['hsId', 'name', 'cardClass', 'classification', 'times_played', 'deck_pop', 'deck_winrate', 'played_winrate', 'extra_data', 'deck_pop_stdev', 'deck_pop_mean', 'update_time']
    list_filter = ['ifanId', 'classification', 'dbfId', 'cost', 'health', 'cardClass', 'rarity', 'type', 'race', 'set', 'artist', 'times_played', 'extra_data', 'update_time']
    search_fields = ['name', 'ename', 'dbfId']
    readonly_fields = ('image_img', 'image_thumb')
    ordering = ('-update_time',)
    list_per_page = 10

class SeriesAdmin(object):
    list_display = ["cname", "ename", "mode", "create_time"]
    list_filter = ["mode", ]
    list_editable = ["mode", ]


xadmin.site.register(Series, SeriesAdmin)
# xadmin.site.register(Cards, CardsAdmin)
xadmin.site.register(HSCards, HSCardsAdmin)
xadmin.site.register(ArenaCards, ArenaCardsAdmin)