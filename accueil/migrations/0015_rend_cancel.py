# Generated by Django 4.0.4 on 2024-03-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0014_rend_l_heure'),
    ]

    operations = [
        migrations.AddField(
            model_name='rend',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]
