# Generated by Django 4.1.3 on 2022-12-14 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_country_school_rename_typp_event_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Major',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='events',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
