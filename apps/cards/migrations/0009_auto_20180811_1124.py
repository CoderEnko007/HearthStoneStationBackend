# Generated by Django 2.0.4 on 2018-08-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20180811_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='series/', verbose_name='扩展包Logo'),
        ),
    ]
