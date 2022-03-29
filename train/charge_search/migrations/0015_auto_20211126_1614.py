# Generated by Django 3.2.8 on 2021-11-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge_search', '0014_auto_20211125_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobanstationmodel',
            name='city',
            field=models.CharField(blank=True, choices=[('[区]東京都区内', '東京都区内'), ('[山]東京山手線内', '東京山手線内')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobanstationmodel',
            name='specific_section',
            field=models.CharField(blank=True, choices=[('東京', '東京'), ('山手線', '山手線'), ('大阪', '大阪'), ('大阪環状線', '大阪環状線')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobanstationmodel',
            name='sta_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobanstationmodel',
            name='sta_name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobanstationmodel',
            name='sta_name_hr',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]