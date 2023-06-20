# Generated by Django 4.2.2 on 2023-06-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_hour_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='day',
            field=models.CharField(choices=[('Mon', 'Lundi'), ('Tue', 'Mardi'), ('Wed', 'Mercredi'), ('Thu', 'Jeudi'), ('Fri', 'Vendredi'), ('Sat', 'Samedi'), ('Sun', 'Dimanche')], max_length=15, unique=True),
        ),
    ]
