# Generated by Django 5.0.7 on 2024-07-21 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0002_alter_contentgeneration_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentgeneration',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
