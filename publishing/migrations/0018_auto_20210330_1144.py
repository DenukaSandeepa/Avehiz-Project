# Generated by Django 2.0.2 on 2021-03-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0017_auto_20210330_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='type',
            field=models.TextField(choices=[('Motorbike', 'Motorbike'), ('Scooter', 'Motorbike'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('MPV/Minivan', 'MPV/Minivan'), ('SUV', 'SUV'), ('CUV/Crossover', 'CUV/Crossover'), ('Pickup', 'Pickup'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Station Wagon', 'Station Wagon'), ('Van', 'Van'), ('Three-Wheeler', 'Three-Wheeler'), ('Lorry', 'Lorry'), ('Bus', 'Bus')], max_length=100),
        ),
    ]
