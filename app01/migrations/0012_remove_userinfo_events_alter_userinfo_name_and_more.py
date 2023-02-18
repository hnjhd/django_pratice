# Generated by Django 4.1.3 on 2022-12-23 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_event_address_alter_event_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='events',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
        migrations.CreateModel(
            name='User_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.userinfo')),
                ('uid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.event')),
            ],
        ),
    ]
