# Generated by Django 2.0.4 on 2018-09-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_auto_20180902_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hscards',
            name='cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='费用'),
        ),
    ]