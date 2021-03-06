# Generated by Django 2.0.2 on 2021-03-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0008_auto_20210322_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='brand',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=100),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='model',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='title',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=100),
        ),
    ]
