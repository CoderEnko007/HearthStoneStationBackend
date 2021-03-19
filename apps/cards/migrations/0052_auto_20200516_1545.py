# Generated by Django 2.0.4 on 2020-05-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0051_hscards_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='hsbattlegroundcards',
            name='ename',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='英文名称'),
        ),
        migrations.AlterField(
            model_name='hsbattlegroundcards',
            name='name',
            field=models.CharField(max_length=100, verbose_name='中文名称'),
        ),
    ]