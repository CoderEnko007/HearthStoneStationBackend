# Generated by Django 2.0.4 on 2020-12-04 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0023_auto_20200410_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='update_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='修改日期'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='添加日期'),
        ),
    ]
