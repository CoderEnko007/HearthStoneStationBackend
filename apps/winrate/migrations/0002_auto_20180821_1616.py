# Generated by Django 2.0.4 on 2018-08-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winrate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hswinrate',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
    ]
