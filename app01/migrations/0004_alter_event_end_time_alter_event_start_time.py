# Generated by Django 4.1.3 on 2022-12-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
