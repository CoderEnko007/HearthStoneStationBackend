# Generated by Django 2.0.4 on 2019-11-05 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0045_hsbattlegroundcards_outtier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsbattlegroundcards',
            name='outTier',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='外部等级'),
        ),
    ]