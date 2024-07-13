# Generated by Django 4.0.4 on 2022-08-21 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0003_rend_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rend',
            old_name='choice',
            new_name='choix',
        ),
        migrations.RenameField(
            model_name='rend',
            old_name='name',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='rend',
            name='La_Date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='rend',
            name='Le_temps',
            field=models.TimeField(default=datetime.time(16, 0)),
        ),
    ]
