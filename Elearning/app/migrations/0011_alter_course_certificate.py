# Generated by Django 5.0.2 on 2024-03-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Certificate',
            field=models.BooleanField(null=True),
        ),
    ]
