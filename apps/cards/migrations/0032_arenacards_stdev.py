# Generated by Django 2.0.4 on 2019-02-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0031_arenacards_extra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='arenacards',
            name='stdev',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='出现率标准差'),
        ),
    ]
