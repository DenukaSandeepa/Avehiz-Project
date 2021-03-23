# Generated by Django 2.0.2 on 2021-03-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0009_auto_20210322_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='address',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=100),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='city',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=50),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='engine',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=50),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='milage',
            field=models.IntegerField(error_messages={'error': "Field Can't Be Empty."}),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='model',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=50),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='price',
            field=models.IntegerField(error_messages={'error': "Field Can't Be Empty."}),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='tel',
            field=models.TextField(error_messages={'error': "Field Can't Be Empty."}, max_length=10),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='year',
            field=models.IntegerField(error_messages={'error': "Field Can't Be Empty."}),
        ),
    ]
