# Generated by Django 2.0.4 on 2018-08-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='img',
            field=models.ImageField(upload_to='cards/full', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='thumbnail',
            field=models.ImageField(upload_to='cards/thumb', verbose_name='缩略图'),
        ),
    ]
