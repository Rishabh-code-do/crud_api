# Generated by Django 4.2.6 on 2024-01-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_box_area_box_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='volume',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
