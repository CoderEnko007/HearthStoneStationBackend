# Generated by Django 2.0.4 on 2019-02-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0030_remove_arenacards_data_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='arenacards',
            name='extra_data',
            field=models.NullBooleanField(verbose_name='统计用数据'),
        ),
    ]
