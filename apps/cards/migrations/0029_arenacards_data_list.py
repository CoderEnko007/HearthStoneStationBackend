# Generated by Django 2.0.4 on 2019-02-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0028_arenacards_ifanid'),
    ]

    operations = [
        migrations.AddField(
            model_name='arenacards',
            name='data_list',
            field=models.TextField(blank=True, null=True, verbose_name='数据列表'),
        ),
    ]