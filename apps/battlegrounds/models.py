from django.db import models
from datetime import datetime
from cards.models import HSBattleGroundCards
# Create your models here.
class Battlegrounds(models.Model):
    RANGE = (
        ('ALL', '所有玩家'),
        ('TOP_50_PERCENT', 'Top 50%'),
        ('TOP_20_PERCENT', 'Top 20%'),
    )
    TIMEFRAME = (
        ('LAST_7_DAYS', '最近7天'),
        ('CURRENT_PATCH', '当前版本')
    )
    TIER = (
        ('T1', '第一梯队'),
        ('T2', '第二梯队'),
        ('T3', '第三梯队'),
        ('T4', '第四梯队')
    )
    mmr_range = models.CharField(max_length=200, default='All', choices=RANGE, verbose_name='MMR Range')
    min_mmr = models.IntegerField(default=0, verbose_name='样本最低分数')
    time_frame = models.CharField(max_length=200, default='Last7Days', choices=TIMEFRAME, verbose_name='时间范围')
    total_games = models.IntegerField(default=0, verbose_name='总对局数')
    tier = models.CharField(max_length=20, choices=TIER, null=True, blank=True, verbose_name='梯队')
    hero = models.ForeignKey(HSBattleGroundCards, related_name='cards', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='英雄')
    num_games_played = models.IntegerField(default=0, verbose_name='使用次数')
    pick_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='选取率')
    popularity = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='热度')
    times_offered = models.IntegerField(default=0, verbose_name='开局出现次数')
    times_chosen = models.IntegerField(default=0, verbose_name='选取次数')
    avg_final_placement = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='平均排名')
    final_placement_distribution = models.TextField(default='', null=True, blank=True, verbose_name='排名分布')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '酒馆战棋英雄数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.hero)
