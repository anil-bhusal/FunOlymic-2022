# Generated by Django 4.0.6 on 2022-09-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_game_gametype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gametype',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.gametype'),
        ),
    ]