# Generated by Django 2.0.4 on 2018-10-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0019_decks_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='decks',
            name='last_30_days',
            field=models.NullBooleanField(help_text='是否为最近30天的数据', verbose_name='最近30天'),
        ),
        migrations.AlterField(
            model_name='decks',
            name='mode',
            field=models.CharField(blank=True, choices=[('Standard', '标准模式'), ('Wild', '狂野模式')], default='Standard', max_length=20, null=True, verbose_name='游戏模式'),
        ),
    ]
