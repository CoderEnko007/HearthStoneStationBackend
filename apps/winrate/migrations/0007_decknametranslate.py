# Generated by Django 2.0.4 on 2018-09-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winrate', '0006_auto_20180824_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeckNameTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction', models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业')),
                ('ename', models.CharField(blank=True, max_length=100, null=True, verbose_name='英文名')),
                ('cname', models.CharField(blank=True, max_length=100, null=True, verbose_name='中文名')),
            ],
            options={
                'verbose_name': '卡组名',
                'verbose_name_plural': '卡组名',
            },
        ),
    ]
