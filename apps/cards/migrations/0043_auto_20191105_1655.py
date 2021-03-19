# Generated by Django 2.0.4 on 2019-11-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0042_hsbattlegroundcards'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hsbattlegroundcards',
            options={'verbose_name': '酒馆战棋卡牌详情', 'verbose_name_plural': '酒馆战棋卡牌详情'},
        ),
        migrations.AddField(
            model_name='hsbattlegroundcards',
            name='gold_image',
            field=models.TextField(blank=True, null=True, verbose_name='金卡地址'),
        ),
        migrations.AddField(
            model_name='hsbattlegroundcards',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='图片地址'),
        ),
    ]