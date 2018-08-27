from django.db import models
from django.utils.html import mark_safe
from utils.globalVar import globalVariable
from datetime import datetime

# Create your models here.
class Decks(models.Model):
    """
    卡组详情
    """
    deck_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='卡组ID')  # 卡组id
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')  # 职业
    deck_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='套牌名称')  # 套牌名称
    dust_cost = models.CharField(max_length=100, null=True, blank=True, verbose_name='合成花费')  # 合成花费
    win_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='胜率')  # 胜率
    game_count = models.IntegerField(null=True, blank=True, verbose_name='总对局数')  # 总对局数
    duration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='对局时长')  # 对局时长
    background_img = models.CharField(max_length=200, null=True, blank=True, verbose_name='背景图')  # 背景图

    card_list = models.TextField(default='', null=True, blank=True, verbose_name='卡组套牌')
    clazzCount = models.TextField(default='', null=True, blank=True, verbose_name='类别组成')
    rarityCount = models.TextField(default='', null=True, blank=True, verbose_name='稀有统计')
    statistic = models.TextField(default='', null=True, blank=True, verbose_name='费用统计')
    turns = models.IntegerField(null=True, blank=True, verbose_name='回合数')
    faction_win_rate = models.TextField(default='', null=True, blank=True, verbose_name='各职业对战胜率')
    create_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = '卡组列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.deck_name
