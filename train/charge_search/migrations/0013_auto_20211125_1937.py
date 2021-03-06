# Generated by Django 3.2.8 on 2021-11-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge_search', '0012_auto_20211124_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobanstationmodel',
            name='city_area',
            field=models.CharField(choices=[('札', '札幌市内'), ('仙', '仙台市内'), ('区', '東京都区内'), ('山', '東京山手線内'), ('浜', '横浜市内'), ('名', '名古屋市内'), ('京', '京都市内'), ('阪', '大阪市内'), ('神', '神戸市内'), ('九', '北九州市内'), ('福', '福岡市内')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='jobanstationmodel',
            name='specific_section',
            field=models.CharField(choices=[('東京', '東京'), ('大阪', '大阪')], max_length=2, null=True),
        ),
    ]
