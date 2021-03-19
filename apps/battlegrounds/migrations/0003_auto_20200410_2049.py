# Generated by Django 2.0.4 on 2020-04-10 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battlegrounds', '0002_auto_20200324_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battlegrounds',
            name='hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='cards.HSBattleGroundCards', verbose_name='英雄'),
        ),
    ]