# Generated by Django 5.0.6 on 2024-06-12 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_management', '0001_initial'),
        ('mechanic_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='mechanic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='mechanic_management.mechanic'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_requests', to='customer_management.customer'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='customer_management.customer'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_requests', to='customer_management.vehicle'),
        ),
    ]
