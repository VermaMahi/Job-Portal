# Generated by Django 5.0.4 on 2024-06-04 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 4, 8, 42, 13, 549718, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
