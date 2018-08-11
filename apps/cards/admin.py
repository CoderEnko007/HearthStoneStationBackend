from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from django.utils.translation import ugettext_lazy as _
# from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
from .models import Cards, Series


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


class CardsAdmin(admin.ModelAdmin):
    list_display = ["cname", "ename", "description", "faction", "clazz", \
                   "race", "rarity", "rule", "series", "mode"]
    list_filter = [
        ('mana', DropdownFilter),
        ('faction', DropdownFilter),
        ('clazz', DropdownFilter),
        ('race', DropdownFilter),
        ('series__cname', DropdownFilter),
        ModeFilter
    ]
    search_fields = ['cname', 'ename']
    readonly_fields = ('image_img','image_thumb') #自定义显示字段，用来显示图片
    exclude = ['img', 'thumbnail'] # 排除该字段
    ordering = ('mana',)
    list_per_page = 30

class SeriesAdmin(admin.ModelAdmin):
    list_display = ["cname", "ename", "create_time"]

admin.site.register(Cards, CardsAdmin)
admin.site.register(Series, SeriesAdmin)