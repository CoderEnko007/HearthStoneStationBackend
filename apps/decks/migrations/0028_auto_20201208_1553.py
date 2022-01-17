# Generated by Django 2.2 on 2020-12-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0027_decks_card_array'),
    ]

    operations = [
        migrations.AddField(
            model_name='decks',
            name='set_array',
            field=models.TextField(blank=True, default='', null=True, verbose_name='包含的扩展包'),
        ),
        migrations.AlterField(
            model_name='decks',
            name='card_array',
            field=models.TextField(blank=True, default='', null=True, verbose_name='包含的单卡id'),
        ),
    ]
