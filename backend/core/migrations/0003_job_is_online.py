# Generated by Django 5.2.4 on 2025-07-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_job_skills_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
