from django.db import models
from datetime import datetime
from utils.globalVar import globalVariable

# Create your models here.
class HSRanking(models.Model):
    faction = models.CharField(max_length=100, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    game_type = models.CharField(max_length=20, choices=globalVariable.MODE_TYPE, null=True, blank=True, verbose_name='游戏模式')
    popularity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='热度')
    win_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='胜率')
    total_games = models.IntegerField(null=True, blank=True, verbose_name='总对局数')
    report_time = models.DateTimeField(default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = 'HS职业胜率排名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-{1}".format(self.game_type, self.faction)



