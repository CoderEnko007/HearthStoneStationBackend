# Generated by Django 2.0.4 on 2018-08-21 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HSWinRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction', models.CharField(blank=True, max_length=20, null=True, verbose_name='职业')),
                ('archetype', models.CharField(blank=True, max_length=20, null=True, verbose_name='卡组模型')),
                ('winrate', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='胜率')),
                ('popularity', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='热度')),
                ('games', models.IntegerField(blank=True, null=True, verbose_name='对局数')),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='日期')),
            ],
            options={
                'verbose_name': '卡组胜率',
                'verbose_name_plural': '卡组胜率',
            },
        ),
    ]
