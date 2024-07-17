# Generated by Django 5.0.6 on 2024-07-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindBestStation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.CharField(max_length=20, unique=True)),
                ('station_name', models.CharField(max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('factor_2', models.FloatField()),
                ('factor_3', models.FloatField()),
                ('factor_4', models.FloatField()),
                ('factor_5', models.FloatField()),
                ('factor_6', models.FloatField()),
                ('factor_7', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='SubwayStation',
        ),
    ]