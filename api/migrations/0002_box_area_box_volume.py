# Generated by Django 4.2.6 on 2024-01-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='box',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]
