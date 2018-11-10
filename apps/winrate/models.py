from django.db import models
from datetime import datetime
from utils.globalVar import globalVariable

# Create your models here.
class HSWinRate(models.Model):
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    archetype = models.CharField(max_length=100, null=True, blank=True, verbose_name='卡组模型')
    winrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='胜率')
    real_winrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='完整胜率')
    popularity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='热度')
    games = models.IntegerField(null=True, blank=True, verbose_name='对局数')
    real_games = models.IntegerField(null=True, blank=True, verbose_name='完整对局数')

    faction_popularity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='职业占比')  # 职业占比
    best_matchup = models.TextField(default='', null=True, blank=True, verbose_name='最优对局')
    worst_matchup = models.TextField(default='', null=True, blank=True, verbose_name='最劣对局')
    pop_deck = models.TextField(default='', null=True, blank=True, verbose_name='最受欢迎卡组')
    best_deck = models.TextField(default='', null=True, blank=True, verbose_name='最优异卡组')
    core_cards = models.TextField(default='', null=True, blank=True, verbose_name='核心卡牌')
    pop_cards = models.TextField(default='', null=True, blank=True, verbose_name='热门卡牌')
    matchup = models.TextField(default='', null=True, blank=True, verbose_name='对抗情况')
    create_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = '卡组胜率'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.archetype


class DeckNameTranslate(models.Model):
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    ename = models.CharField(max_length=100, null=True, blank=True, verbose_name='英文名')
    cname = models.CharField(max_length=100, null=True, blank=True, verbose_name='中文名')
    create_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = '卡组名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ename