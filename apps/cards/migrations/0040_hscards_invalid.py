# Generated by Django 2.0.4 on 2019-06-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0039_hscards_entourage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hscards',
            name='invalid',
            field=models.BooleanField(default=False, verbose_name='无效卡'),
        ),
    ]
