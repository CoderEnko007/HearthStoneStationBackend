# Generated by Django 2.0.4 on 2018-08-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20180809_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='thumbnail',
            field=models.ImageField(upload_to='', verbose_name='缩略图'),
        ),
    ]
