from django.db import models
from django.utils.html import mark_safe
from datetime import datetime

# Create your models here.
class Series(models.Model):
    """
    扩展包详情
    """
    cname = models.CharField(max_length=20, default='', verbose_name='扩展包（中文）')
    ename = models.CharField(max_length=20, default='', verbose_name='扩展包（英文）')
    image = models.ImageField(max_length=200, null=True, blank=True, upload_to='series/', verbose_name='扩展包Logo')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '扩展包名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname


class Cards(models.Model):
    """
    卡牌详情
    """
    MODE_TYPE = (
        ('Standard', '标准模式'),
        ('Wild', '狂野模式')
    )
    FACTION_TYPE = (
        ('Druid', '德鲁伊'),
        ('Hunter', '猎人'),
        ('Mage', '法师'),
        ('Paladin', '圣骑士'),
        ('Priest', '牧师'),
        ('Rogue', '潜行者'),
        ('Shaman', '萨满'),
        ('Warlock', '术士'),
        ('Warrior', '战士'),
        ('Neutral', '中立')
    )
    RARITY_TYPE = (
        ('1', '基本'),
        ('2', '普通'),
        ('3', '稀有'),
        ('4', '史诗'),
        ('5', '传说'),
    )
    mana = models.IntegerField(default=0, verbose_name='费用') # 费用
    hp = models.IntegerField(default=0, verbose_name='血量') # 血量
    attack = models.IntegerField(default=0, verbose_name='伤害') # 伤害
    cname = models.CharField(max_length=100, verbose_name='名称')  # 名称
    description = models.CharField(max_length=300, default='', verbose_name='描述')  # 描述
    ename = models.CharField(max_length=100, default='', verbose_name='英文名')  # 英文名
    faction = models.CharField(max_length=20, choices=FACTION_TYPE, default='', verbose_name='职业')  # 职业
    clazz = models.CharField(max_length=20, default='', verbose_name='卡牌类别')  # 卡牌类别
    race = models.CharField(max_length=20, default='', verbose_name='种族')  # 种族
    rarity = models.CharField(max_length=20, choices=RARITY_TYPE, default='', verbose_name='稀有度')  # 稀有度
    rule = models.CharField(max_length=300, default='', verbose_name='卡牌效果说明')  # 卡牌效果说明
    # seriesAbbr = models.CharField(max_length=20, default='', verbose_name='扩展包（英文）')
    # seriesName = models.CharField(max_length=20, default='', verbose_name='扩展包（中文）')
    # standard = models.NullBooleanField(null=True, blank=True, verbose_name='标准模式')
    # wild = models.NullBooleanField(null=True, blank=True, verbose_name='狂野模式')
    series = models.ForeignKey(Series, related_name='cards', default='', verbose_name='扩展包系列', on_delete=models.SET_DEFAULT)
    mode = models.CharField(max_length=20, null=True, blank=True, choices=MODE_TYPE, verbose_name='游戏模式', help_text='游戏模式')

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
