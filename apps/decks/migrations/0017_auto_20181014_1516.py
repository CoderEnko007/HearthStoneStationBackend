# Generated by Django 2.0.4 on 2018-10-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0016_auto_20181011_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trending',
            name='dust_cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='合成花费'),
        ),
    ]
