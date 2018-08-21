from django.db import models
from datetime import datetime
from utils.globalVar import globalVariable

# Create your models here.
class HSWinRate(models.Model):
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    archetype = models.CharField(max_length=20, null=True, blank=True, verbose_name='卡组模型')
    winrate = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name='胜率')
    popularity = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name='热度')
    games = models.IntegerField(null=True, blank=True, verbose_name='对局数')
    create_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = '卡组胜率'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.archetype