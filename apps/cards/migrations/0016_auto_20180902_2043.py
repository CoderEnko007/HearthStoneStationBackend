# Generated by Django 2.0.4 on 2018-09-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_hscards_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='hscards',
            name='hsId',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='hsId'),
        ),
        migrations.AlterField(
            model_name='hscards',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]