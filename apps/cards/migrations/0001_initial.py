# Generated by Django 2.1 on 2018-08-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mana', models.IntegerField(default=0, verbose_name='费用')),
                ('hp', models.IntegerField(default=0, verbose_name='血量')),
                ('attack', models.IntegerField(default=0, verbose_name='伤害')),
                ('cname', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.CharField(max_length=300, verbose_name='描述')),
                ('ename', models.CharField(max_length=100, verbose_name='英文名')),
                ('faction', models.CharField(max_length=20, verbose_name='职业')),
                ('clazz', models.CharField(max_length=20, verbose_name='卡牌类别')),
                ('race', models.CharField(max_length=20, verbose_name='种族')),
                ('rarity', models.CharField(max_length=20, verbose_name='稀有度')),
                ('rule', models.CharField(max_length=300, verbose_name='卡牌效果说明')),
                ('seriesAbbr', models.CharField(max_length=20, verbose_name='系列简称')),
                ('seriesName', models.CharField(max_length=20, verbose_name='系列中文全名')),
                ('img', models.CharField(max_length=300, verbose_name='图片')),
                ('thumbnail', models.CharField(max_length=300, verbose_name='缩略图')),
            ],
            options={
                'verbose_name': '卡牌详情',
                'verbose_name_plural': '卡牌详情',
            },
        ),
    ]
