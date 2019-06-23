from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from django.utils.translation import ugettext_lazy as _
from daterange_filter.filter import DateRangeFilter
# from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
from .models import HSCards, Series, ArenaCards


class ModeFilter(admin.SimpleListFilter):
    title = _(u'游戏模式')
    parameter_name = 'standard'

    def lookups(self, request, model_admin):
        return (
            ('0', _(u'狂野模式')),
            ('1', _(u'标准模式'))
        )
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(mode__in=['Standard', 'Wild'])
        if self.value() == '1':
            return queryset.filter(mode='Standard')

class CardsClassFilter(admin.SimpleListFilter):
    title = _(u'职业卡分类')
    parameter_name = 'card_class'

    def lookups(self, request, model_admin):
        return (
            ('0', _('职业卡')),
            ('1', _('非职业卡'))
        )
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(cardClass__in=['Druid', 'Hunter', 'Mage', 'Paladin', 'Priest', 'Rogue', 'Shaman', 'Warlock', 'Warrior'])
        else:
            return queryset

class CardsAdmin(admin.ModelAdmin):
    list_display = ['hsId', 'name', 'ename', 'cardClass', 'rarity', 'type', 'race', 'text', 'set', 'img_tile_link', 'img_card_link']
    list_filter = [
        ('cardClass', DropdownFilter),
        ('race', DropdownFilter),
        ('set__cname', DropdownFilter),
        ModeFilter
    ]
    search_fields = ['name', 'ename']
    readonly_fields = ('image_img','image_thumb') #自定义显示字段，用来显示图片
    exclude = ['img', 'thumbnail'] # 排除该字段
    ordering = ('cost',)
    list_per_page = 30

class ArenaCardsAdmin(admin.ModelAdmin):
    list_display = ['hsId', 'name', 'cardClass', 'classification', 'times_played', 'deck_pop', 'deck_winrate',
                    'played_winrate', 'extra_data', 'deck_pop_stdev', 'deck_pop_mean', 'update_time']
    list_filter = [
        ('cardClass', DropdownFilter),
        ('classification', DropdownFilter),
        ('extra_data', DropdownFilter),
        ('update_time', DateRangeFilter),
        CardsClassFilter,
        'update_time'
    ]
    search_fields = ['name', 'ename', 'dbfId']
    readonly_fields = ('image_img', 'image_thumb')
    ordering = ('-update_time',)
    list_per_page = 10

class SeriesAdmin(admin.ModelAdmin):
    list_display = ["cname", "ename", "create_time"]

admin.site.register(HSCards, CardsAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(ArenaCards, ArenaCardsAdmin)