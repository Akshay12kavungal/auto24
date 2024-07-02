# Generated by Django 5.0.6 on 2024-07-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='rental_cars/')),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
