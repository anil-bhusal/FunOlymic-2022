# Generated by Django 4.0.6 on 2022-09-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funolympicgame2022', '0014_rename_gamename_schedule_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='news',
            field=models.TextField(blank=True, null=True),
        ),
    ]
