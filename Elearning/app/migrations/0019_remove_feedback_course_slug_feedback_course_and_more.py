# Generated by Django 5.0.2 on 2024-05-04 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_feedback_course_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='course_slug',
        ),
        migrations.AddField(
            model_name='feedback',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
