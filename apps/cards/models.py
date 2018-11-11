from django.db import models
from django.utils.html import mark_safe
from datetime import datetime
from utils.globalVar import globalVariable

# Create your models here.
class Series(models.Model):
    """
    扩展包详情
    """
    cname = models.CharField(max_length=20, default='', verbose_name='扩展包（中文）')
    ename = models.CharField(max_length=20, default='', verbose_name='扩展包（英文）')
    image = models.ImageField(max_length=200, null=True, blank=True, upload_to='series/', verbose_name='扩展包Logo')
    mode = models.CharField(max_length=20, null=True, blank=True, choices=globalVariable.MODE_TYPE, verbose_name='游戏模式', help_text='游戏模式')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '扩展包'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname


class Cards(models.Model):
    """
    卡牌详情
    """
    mana = models.IntegerField(default=0, verbose_name='费用') # 费用
    hp = models.IntegerField(default=0, verbose_name='血量') # 血量
    attack = models.IntegerField(default=0, verbose_name='伤害') # 伤害
    cname = models.CharField(max_length=100, verbose_name='名称')  # 名称
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='描述')  # 描述
    ename = models.CharField(max_length=100, null=True, blank=True, verbose_name='英文名')  # 英文名
    faction = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')  # 职业
    clazz = models.CharField(max_length=20, null=True, blank=True, choices=globalVariable.CLAZZ_TYPE, verbose_name='卡牌类别')  # 卡牌类别
    race = models.CharField(max_length=20, null=True, blank=True, verbose_name='种族')  # 种族
    rarity = models.CharField(max_length=20, choices=globalVariable.RARITY_TYPE, null=True, blank=True, verbose_name='稀有度')  # 稀有度
    rule = models.CharField(max_length=300, null=True, blank=True, verbose_name='卡牌效果说明')  # 卡牌效果说明
    series = models.ForeignKey(Series, related_name='cards', null=True, blank=True, verbose_name='扩展包系列', on_delete=models.SET_NULL)
    mode = models.CharField(max_length=20, null=True, blank=True, choices=globalVariable.MODE_TYPE, verbose_name='游戏模式', help_text='游戏模式')

    img = models.CharField(max_length=300, verbose_name='图片')  # 图片
    thumbnail = models.CharField(max_length=300, verbose_name='缩略图')  # 缩略图

    def image_img(self):
        if self.img:
            return mark_safe('<img src="%s" />' % self.img)
        else:
            return '(no image)'
    image_img.short_description = '图片'

    def image_thumb(self):
        if self.thumbnail:
            return mark_safe('<img src="%s" />' % self.thumbnail)
        else:
            return '(no image)'
    image_thumb.short_description = '缩略图'

    class Meta:
        verbose_name = '卡牌详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname


class HSCards(models.Model):
    hsId = models.CharField(max_length=20, null=True, blank=True, verbose_name='hsId')
    dbfId = models.IntegerField(verbose_name='DBF IDs')
    name = models.CharField(max_length=100, verbose_name='名称')
    ename = models.CharField(max_length=100, null=True, blank=True, verbose_name='英文名')
    cost = models.IntegerField(null=True, blank=True, verbose_name='费用')
    attack = models.IntegerField(null=True, blank=True, verbose_name='攻击')
    health = models.IntegerField(null=True, blank=True, verbose_name='血量')
    cardClass = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True, verbose_name='职业')
    race = models.CharField(max_length=20, null=True, blank=True, verbose_name='种族')
    rarity = models.CharField(max_length=20, choices=globalVariable.RARITY_TYPE, verbose_name='稀有度')
    set = models.ForeignKey(Series, related_name='HSCards', null=True, blank=True, verbose_name='扩展包系列', on_delete=models.SET_NULL)
    type = models.CharField(max_length=20, null=True, blank=True, choices=globalVariable.CLAZZ_TYPE, verbose_name='卡牌类别')
    mechanics = models.TextField(null=True, blank=True, verbose_name='卡牌机制')
    flavor = models.TextField(null=True, blank=True, verbose_name='描述')
    text = models.TextField(null=True, blank=True, verbose_name='效果')
    artist = models.CharField(max_length=200, null=True, blank=True, verbose_name='艺术家')
    collectible = models.BooleanField(verbose_name='可收集')

    def image_img(self):
        if self.hsId:
            str = "<img src='https://art.hearthstonejson.com/v1/256x/{}.jpg'/>".format(self.hsId)
            return mark_safe(str)
        else:
            return '(no image)'
    image_img.short_description = '图片'

    def image_thumb(self):
        if self.hsId:
            str = "<img src='https://art.hearthstonejson.com/v1/tiles/{}.jpg'/>".format(self.hsId)
            return mark_safe(str)
        else:
            return '(no image)'
    image_thumb.short_description = '缩略图'

    class Meta:
        verbose_name = '卡牌详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ArenaCards(models.Model):
    hsId = models.CharField(max_length=20, null=True, blank=True, verbose_name='hsId')
    dbfId = models.IntegerField(verbose_name='DBF IDs')
    name = models.CharField(max_length=100, verbose_name='名称')
    ename = models.CharField(max_length=100, null=True, blank=True, verbose_name='英文名')
    cost = models.IntegerField(null=True, blank=True, verbose_name='费用')
    attack = models.IntegerField(null=True, blank=True, verbose_name='攻击')
    health = models.IntegerField(null=True, blank=True, verbose_name='血量')
    cardClass = models.CharField(max_length=20, choices=globalVariable.FACTION_TYPE, null=True, blank=True,
                                 verbose_name='职业')
    race = models.CharField(max_length=20, null=True, blank=True, verbose_name='种族')
    rarity = models.CharField(max_length=20, choices=globalVariable.RARITY_TYPE, verbose_name='稀有度')
    set = models.ForeignKey(Series, related_name='ArenaCards', null=True, blank=True, verbose_name='扩展包系列',
                            on_delete=models.SET_NULL)
    type = models.CharField(max_length=20, null=True, blank=True, choices=globalVariable.CLAZZ_TYPE,
                            verbose_name='卡牌类别')
    mechanics = models.TextField(null=True, blank=True, verbose_name='卡牌机制')
    flavor = models.TextField(null=True, blank=True, verbose_name='描述')
    text = models.TextField(null=True, blank=True, verbose_name='效果')
    artist = models.CharField(max_length=200, null=True, blank=True, verbose_name='艺术家')
    collectible = models.BooleanField(verbose_name='可收集')

    classification = models.CharField(max_length=20, choices=globalVariable.ARENA_FACTION_TYPE, verbose_name='职业分类')
    times_played = models.IntegerField(null=True, blank=True, verbose_name='打出次数')
    played_pop = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='打出卡牌中占比')
    played_winrate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='打出胜率')
    deck_pop = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='套牌中出现概率')
    deck_winrate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='卡组胜率')
    copies = models.IntegerField(null=True, blank=True, verbose_name='张数')

    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    def image_img(self):
        if self.hsId:
            str = "<img src='https://art.hearthstonejson.com/v1/256x/{}.jpg'/>".format(self.hsId)
            return mark_safe(str)
        else:
            return '(no image)'
    image_img.short_description = '图片'

    def image_thumb(self):
        if self.hsId:
            str = "<img src='https://art.hearthstonejson.com/v1/tiles/{}.jpg'/>".format(self.hsId)
            return mark_safe(str)
        else:
            return '(no image)'
    image_thumb.short_description = '缩略图'

    class Meta:
        verbose_name = '竞技场单卡数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name