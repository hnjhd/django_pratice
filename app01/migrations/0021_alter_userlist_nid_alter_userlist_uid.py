# Generated by Django 4.1.3 on 2022-12-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0020_remove_userlist_address_remove_userlist_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='nid',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='uid',
            field=models.IntegerField(default=10),
        ),
    ]
