# Generated by Django 2.0.4 on 2019-11-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0043_auto_20191105_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='hsbattlegroundcards',
            name='parentID',
            field=models.IntegerField(blank=True, null=True, verbose_name='归属卡牌ID'),
        ),
    ]