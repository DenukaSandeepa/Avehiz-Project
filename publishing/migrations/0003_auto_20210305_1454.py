# Generated by Django 2.0.2 on 2021-03-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0002_auto_20210303_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishing',
            name='boday',
        ),
        migrations.RemoveField(
            model_name='publishing',
            name='url',
        ),
        migrations.AddField(
            model_name='publishing',
            name='brand',
            field=models.IntegerField(choices=[('0', 'Car'), ('1', 'Suv')], default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='publishing',
            name='engine',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='publishing',
            name='fuel',
            field=models.IntegerField(choices=[('0', 'Car'), ('1', 'Suv')], default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='milage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='model',
            field=models.IntegerField(choices=[('0', 'Car'), ('1', 'Suv')], default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='transmission',
            field=models.IntegerField(choices=[('0', 'Car'), ('1', 'Suv')], default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='type',
            field=models.IntegerField(choices=[('0', 'Car'), ('1', 'Suv')], default=0),
        ),
        migrations.AddField(
            model_name='publishing',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='icon',
            field=models.ImageField(upload_to='upload_to=images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload_to=images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
