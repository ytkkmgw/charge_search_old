# Generated by Django 3.2.8 on 2021-11-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge_search', '0009_alter_jobanstationmodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacivFareModel',
            fields=[
                ('fare_type', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fare_3', models.IntegerField()),
                ('fare_6', models.IntegerField()),
                ('fare_10', models.IntegerField()),
                ('fare_15', models.IntegerField()),
                ('fare_20', models.IntegerField()),
                ('fare_25', models.IntegerField()),
                ('fare_30', models.IntegerField()),
                ('fare_35', models.IntegerField()),
                ('fare_40', models.IntegerField()),
                ('fare_45', models.IntegerField()),
                ('fare_50', models.IntegerField()),
                ('fare_60', models.IntegerField()),
                ('fare_70', models.IntegerField()),
                ('fare_80', models.IntegerField()),
                ('fare_90', models.IntegerField()),
                ('fare_100', models.IntegerField()),
                ('fare_120', models.IntegerField()),
                ('fare_140', models.IntegerField()),
                ('fare_160', models.IntegerField()),
                ('fare_180', models.IntegerField()),
                ('fare_200', models.IntegerField()),
                ('fare_220', models.IntegerField()),
                ('fare_240', models.IntegerField()),
                ('fare_260', models.IntegerField()),
                ('fare_280', models.IntegerField()),
                ('fare_300', models.IntegerField()),
                ('fare_320', models.IntegerField()),
                ('fare_340', models.IntegerField()),
                ('fare_360', models.IntegerField()),
                ('fare_380', models.IntegerField()),
                ('fare_400', models.IntegerField()),
            ],
        ),
    ]
