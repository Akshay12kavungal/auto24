# Generated by Django 5.0.6 on 2024-07-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
