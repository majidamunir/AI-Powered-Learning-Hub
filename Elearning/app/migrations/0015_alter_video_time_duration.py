# Generated by Django 5.0.2 on 2024-04-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_video_time_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time_duration',
            field=models.IntegerField(null=True),
        ),
    ]
