# Generated by Django 2.0.2 on 2021-03-23 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0014_auto_20210323_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
