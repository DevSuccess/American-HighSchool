# Generated by Django 4.2.2 on 2023-06-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_about_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='libel',
            field=models.TextField(null=True),
        ),
    ]
