# Generated by Django 4.0.4 on 2022-09-04 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0006_remove_rend_username_alter_rend_téléphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rend',
            name='La_Date',
        ),
        migrations.RemoveField(
            model_name='rend',
            name='Le_temps',
        ),
        migrations.RemoveField(
            model_name='rend',
            name='Raison',
        ),
    ]