# Generated by Django 2.0.4 on 2020-03-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archetype', '0010_auto_20190901_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archetype',
            options={'verbose_name': '梯队信息', 'verbose_name_plural': '梯队信息'},
        ),
        migrations.AlterField(
            model_name='archetype',
            name='faction',
            field=models.CharField(blank=True, choices=[('Druid', '德鲁伊'), ('Hunter', '猎人'), ('Mage', '法师'), ('Paladin', '圣骑士'), ('Priest', '牧师'), ('Rogue', '潜行者'), ('Shaman', '萨满'), ('Warlock', '术士'), ('Warrior', '战士'), ('Demonhunter', '恶魔猎手'), ('Neutral', '中立')], max_length=20, null=True, verbose_name='职业'),
        ),
    ]
