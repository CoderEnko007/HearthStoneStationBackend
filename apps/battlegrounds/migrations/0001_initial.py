# Generated by Django 2.0.4 on 2020-03-23 16:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0047_auto_20200227_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battlegrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mmr_range', models.CharField(choices=[('All', '所有玩家'), ('Top50', 'Top 50%'), ('Top20', 'Top 20%')], default='All', max_length=200, verbose_name='MMR Range')),
                ('time_frame', models.CharField(choices=[('Last7Days', '最近7天'), ('CurrentPatch', '当前版本')], default='Last7Days', max_length=200, verbose_name='时间范围')),
                ('total_games', models.IntegerField(default=0, verbose_name='总对局数')),
                ('tier', models.CharField(blank=True, max_length=20, null=True, verbose_name='梯队')),
                ('num_games_played', models.IntegerField(default=0, verbose_name='使用次数')),
                ('pick_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='选取率')),
                ('popularity', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='热度')),
                ('times_offered', models.IntegerField(default=0, verbose_name='开局出现次数')),
                ('times_chosen', models.IntegerField(default=0, verbose_name='选取次数')),
                ('avg_final_placement', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='平均排名')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='battlegrounds', to='cards.HSBattleGroundCards', verbose_name='英雄')),
            ],
            options={
                'verbose_name': '酒馆战棋英雄',
                'verbose_name_plural': '酒馆战棋英雄',
            },
        ),
    ]
