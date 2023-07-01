# Generated by Django 4.2.2 on 2023-07-01 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_alter_aboutitti_options_alter_aboutitti_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'Les Missions et Visions'},
        ),
        migrations.AlterModelOptions(
            name='aboutahsm',
            options={'verbose_name_plural': 'Les Informations sur AHSH'},
        ),
        migrations.AlterModelOptions(
            name='abouthelp',
            options={'verbose_name_plural': "Les Supports d'Aide Client (About) "},
        ),
        migrations.AlterModelTable(
            name='about',
            table='about_us',
        ),
        migrations.AlterModelTable(
            name='aboutahsm',
            table='about_ahsm',
        ),
        migrations.AlterModelTable(
            name='abouthelp',
            table='about_help',
        ),
    ]
