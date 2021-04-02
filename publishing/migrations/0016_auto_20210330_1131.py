# Generated by Django 2.0.2 on 2021-03-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0015_auto_20210323_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='type',
            field=models.TextField(choices=[('Motorbike', 'Motorbike'), ('Motorbike-Scooter', 'Motorbike-Scooter'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('MPV/Minivan', 'MPV/Minivan'), ('SUV', 'SUV'), ('CUV/Crossover', 'CUV/Crossover'), ('Pickup', 'Pickup'), ('Coupe', 'Coupe'), ('Convertible/Spyder/Cabriolet', 'Convertible/Spyder/Cabriolet'), ('Station Wagon/Estate', 'Station Wagon/Estate'), ('Van', 'Van'), ('Three-Wheeler', 'Three-Wheeler'), ('Lorry', 'Lorry'), ('Bus', 'Bus')], max_length=100),
        ),
    ]