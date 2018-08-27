from django.db import models
from datetime import datetime
from utils.globalVar import globalVariable

# Create your models here.
class HSRanking(models.Model):
    mode = models.CharField(max_length=20, choices=globalVariable.MODE_TYPE, null=True, blank=True, verbose_name='游戏模式')
    rank_no = models.IntegerField(null=True, blank=True, verbose_name='排名')
    name = models.CharField(max_length=100, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    winrate = models.CharField(max_length=20, null=True, blank=True, verbose_name='胜率')
    report_time = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='日期')

    class Meta:
        verbose_name = 'HS职业胜率排名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-{1}".format(self.mode, self.name)



