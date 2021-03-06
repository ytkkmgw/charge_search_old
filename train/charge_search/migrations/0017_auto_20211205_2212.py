# Generated by Django 3.2.8 on 2021-12-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge_search', '0016_auto_20211130_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokaidoStationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sta_name', models.CharField(blank=True, max_length=20, null=True)),
                ('sta_name_hr', models.CharField(blank=True, max_length=30, null=True)),
                ('distance', models.FloatField()),
                ('city', models.CharField(blank=True, choices=[('[札]札幌市内', '札幌市内'), ('[仙]仙台市内', '仙台市内'), ('[区]東京都区内', '東京都区内'), ('[山]東京山手線内', '東京山手線内'), ('[浜]横浜市内', '横浜市内'), ('[名]名古屋市内', '名古屋市内'), ('[京]京都市内', '京都市内'), ('[阪]大阪市内', '大阪市内'), ('[神]神戸市内', '神戸市内'), ('[広]広島市内', '広島市内'), ('[九]北九州市内', '北九州市内'), ('[福]福岡市内', '福岡市内')], max_length=50, null=True)),
                ('specific_section', models.CharField(blank=True, choices=[('東京', '東京'), ('山手線', '山手線'), ('大阪', '大阪'), ('大阪環状線', '大阪環状線')], max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobanstationmodel',
            name='sta_name_en',
        ),
    ]
