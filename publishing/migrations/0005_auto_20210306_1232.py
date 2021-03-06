# Generated by Django 2.0.2 on 2021-03-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0004_auto_20210305_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='brand',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='condition',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='fuel',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='icon',
            field=models.ImageField(blank=True, upload_to='upload_to=images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='model',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='transmission',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='type',
            field=models.TextField(blank=True),
        ),
    ]
