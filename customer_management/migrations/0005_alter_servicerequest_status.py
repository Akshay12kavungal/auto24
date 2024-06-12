# Generated by Django 5.0.6 on 2024-06-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0004_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=20),
        ),
    ]