# Generated by Django 5.2.4 on 2025-07-29 12:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postimage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
