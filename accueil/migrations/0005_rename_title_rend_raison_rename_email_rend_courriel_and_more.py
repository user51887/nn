# Generated by Django 4.0.4 on 2022-09-04 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0004_rename_choice_rend_choix_rename_name_rend_nom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rend',
            old_name='title',
            new_name='Raison',
        ),
        migrations.RenameField(
            model_name='rend',
            old_name='email',
            new_name='courriel',
        ),
        migrations.RenameField(
            model_name='rend',
            old_name='password',
            new_name='téléphone',
        ),
    ]
