# Generated by Django 5.0.6 on 2024-06-11 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='mechanic',
            name='user',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='service_request',
        ),
        migrations.RemoveField(
            model_name='mechanicwork',
            name='mechanic',
        ),
        migrations.RemoveField(
            model_name='mechanicwork',
            name='service_request',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Mechanic',
        ),
        migrations.DeleteModel(
            name='MechanicWork',
        ),
        migrations.DeleteModel(
            name='ServiceRequest',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
