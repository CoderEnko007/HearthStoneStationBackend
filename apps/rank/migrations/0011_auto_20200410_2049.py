# Generated by Django 2.0.4 on 2020-04-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0010_auto_20200330_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsranking',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=100, null=True, verbose_name='职业'),
        ),
    ]
