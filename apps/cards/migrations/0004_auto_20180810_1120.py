# Generated by Django 2.0.4 on 2018-08-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20180809_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='standard',
            field=models.BooleanField(default=0, verbose_name='标准模式'),
        ),
        migrations.AddField(
            model_name='cards',
            name='wild',
            field=models.BooleanField(default=1, verbose_name='狂野模式'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='clazz',
            field=models.CharField(default='', max_length=20, verbose_name='卡牌类别'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='description',
            field=models.CharField(default='', max_length=300, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='ename',
            field=models.CharField(default='', max_length=100, verbose_name='英文名'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='faction',
            field=models.CharField(default='', max_length=20, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='img',
            field=models.ImageField(upload_to='cards/full', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='race',
            field=models.CharField(default='', max_length=20, verbose_name='种族'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='rarity',
            field=models.CharField(default='', max_length=20, verbose_name='稀有度'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='rule',
            field=models.CharField(default='', max_length=300, verbose_name='卡牌效果说明'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='seriesAbbr',
            field=models.CharField(default='', max_length=20, verbose_name='系列简称'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='seriesName',
            field=models.CharField(default='', max_length=20, verbose_name='系列中文全名'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='thumbnail',
            field=models.ImageField(upload_to='cards/thumb', verbose_name='缩略图'),
        ),
    ]
