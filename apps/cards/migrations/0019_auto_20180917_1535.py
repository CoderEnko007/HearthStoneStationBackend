# Generated by Django 2.0.4 on 2018-09-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_series_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='mode',
            field=models.CharField(blank=True, choices=[('All', '全部模式'), ('Standard', '标准模式'), ('Wild', '狂野模式'), ('Arena', '竞技场')], help_text='游戏模式', max_length=20, null=True, verbose_name='游戏模式'),
        ),
        migrations.AlterField(
            model_name='series',
            name='mode',
            field=models.CharField(blank=True, choices=[('All', '全部模式'), ('Standard', '标准模式'), ('Wild', '狂野模式'), ('Arena', '竞技场')], help_text='游戏模式', max_length=20, null=True, verbose_name='游戏模式'),
        ),
    ]
