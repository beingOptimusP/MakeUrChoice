# Generated by Django 3.1.7 on 2021-03-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0003_auto_20210327_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatpoll',
            name='on2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='creatpoll',
            name='on3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='creatpoll',
            name='on4',
            field=models.IntegerField(default=0),
        ),
    ]
