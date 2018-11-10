from django.db import models
from utils.globalVar import globalVariable
from datetime import datetime

# Create your models here.
class Archetype(models.Model):
    tier = models.CharField(max_length=20, null=True, blank=True, verbose_name='梯队')
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    archetype_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='牌组名称')
    win_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='胜率')  # 胜率
    game_count = models.IntegerField(null=True, blank=True, verbose_name='总对局数')  # 总对局数
    popularity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='热度')  # 胜率
    best_matchup = models.TextField(default='', null=True, blank=True, verbose_name='最优对局')
    worst_matchup = models.TextField(default='', null=True, blank=True, verbose_name='最劣对局')
    pop_deck = models.TextField(default='', null=True, blank=True, verbose_name='最受欢迎卡组')
    best_deck = models.TextField(default='', null=True, blank=True, verbose_name='最优异卡组')
    core_cards =  models.TextField(default='', null=True, blank=True, verbose_name='核心卡牌')
    pop_cards = models.TextField(default='', null=True, blank=True, verbose_name='热门卡牌')
    matchup = models.TextField(default='', null=True, blank=True, verbose_name='对抗情况')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '卡组模板数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.archetype_name