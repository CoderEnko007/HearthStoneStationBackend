# Generated by Django 2.0.4 on 2018-08-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archetype', '0004_auto_20180824_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archetype',
            name='popularity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='热度'),
        ),
        migrations.AlterField(
            model_name='archetype',
            name='win_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='胜率'),
        ),
    ]
