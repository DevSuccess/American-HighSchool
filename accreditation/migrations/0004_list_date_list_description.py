# Generated by Django 4.2.2 on 2023-06-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0003_alter_list_options_alter_list_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
