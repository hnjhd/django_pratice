# Generated by Django 4.1.3 on 2022-12-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_alter_userlist_nid_alter_userlist_uid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserList',
        ),
    ]
