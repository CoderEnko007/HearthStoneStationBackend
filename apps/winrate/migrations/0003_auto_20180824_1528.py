# Generated by Django 2.0.4 on 2018-08-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winrate', '0002_auto_20180821_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hswinrate',
            name='archetype',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='卡组模型'),
        ),
    ]
