# Generated by Django 2.0.4 on 2020-04-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0049_auto_20200330_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arenacards',
            name='cardClass',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='hscards',
            name='cardClass',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('DemonHunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
    ]
