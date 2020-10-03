# Generated by Django 2.0.4 on 2020-08-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0052_auto_20200516_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='hscards',
            name='classes',
            field=models.TextField(blank=True, null=True, verbose_name='多职业'),
        ),
        migrations.AlterField(
            model_name='hsbattlegroundcards',
            name='minionType',
            field=models.CharField(blank=True, choices=[('14', '鱼人'), ('15', '恶魔'), ('17', '机械'), ('20', '野兽'), ('24', '龙'), ('26', '全部'), ('23', '海盗')], max_length=20, null=True, verbose_name='随从种类'),
        ),
    ]
