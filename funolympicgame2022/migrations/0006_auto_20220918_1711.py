# Generated by Django 3.2 on 2022-09-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funolympicgame2022', '0005_schedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='game',
            new_name='game1',
        ),
        migrations.AddField(
            model_name='schedule',
            name='game2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='game3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
    ]