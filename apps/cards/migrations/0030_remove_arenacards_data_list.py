# Generated by Django 2.0.4 on 2019-02-10 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0029_arenacards_data_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arenacards',
            name='data_list',
        ),
    ]
