# Generated by Django 2.0.4 on 2018-09-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0013_auto_20180920_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='decks',
            name='trending_flag',
            field=models.BooleanField(default=False, verbose_name='48小时流行卡组'),
        ),
    ]