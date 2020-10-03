# Generated by Django 2.0.4 on 2020-04-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winrate', '0017_auto_20200403_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hswinrate',
            name='rank_range',
            field=models.CharField(choices=[('All', '全分段'), ('Legend_Only', '传说分段'), ('One_Through_Five', '5级-1级分段'), ('Six_Through_Ten', '10级-6级分段'), ('BRONZE_THROUGH_GOLD', '青铜-黄金'), ('PLATINUM_THROUGH_LEGEND', '白金-传说'), ('LEGEND', '传说')], default='BRONZE_TO_GOLD', max_length=200, verbose_name='排名分段'),
        ),
    ]
