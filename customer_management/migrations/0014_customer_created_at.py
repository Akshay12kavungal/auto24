# Generated by Django 5.0.6 on 2024-07-05 10:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0013_alter_servicerequest_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
