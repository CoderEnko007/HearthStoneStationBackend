# Generated by Django 2.0.4 on 2019-06-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0037_auto_20190619_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hscards',
            old_name='update_time',
            new_name='create_time',
        ),
    ]
