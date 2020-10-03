# Generated by Django 2.0.4 on 2020-04-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winrate', '0019_auto_20200403_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decknametranslate',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='hswinrate',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='hswinrate',
            name='rank_range',
            field=models.CharField(choices=[('All', '全分段'), ('Legend_Only', '传说分段'), ('One_Through_Five', '5级-1级分段'), ('Six_Through_Ten', '10级-6级分段'), ('BRONZE_THROUGH_GOLD', '青铜-黄金'), ('DIAMOND_THROUGH_LEGEND', '钻石-传说'), ('LEGEND', '传说')], default='BRONZE_THROUGH_GOLD', max_length=200, verbose_name='排名分段'),
        ),
    ]
