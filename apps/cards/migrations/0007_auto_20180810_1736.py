# Generated by Django 2.0.4 on 2018-08-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20180810_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='img',
            field=models.CharField(max_length=300, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='thumbnail',
            field=models.CharField(max_length=300, verbose_name='缩略图'),
        ),
    ]
