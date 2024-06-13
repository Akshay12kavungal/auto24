from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/MechanicProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    skill = models.CharField(max_length=500, null=True)
    salary = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.user.first_name

class MechanicWork(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='works')
    service_request = models.ForeignKey('customer_management.ServiceRequest', on_delete=models.CASCADE, related_name='works')
    assigned_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('Repairing', 'Repairing'),
        ('Repairing Done', 'Repairing Done'),
        ('Released', 'Released')
    ], default='Repairing')
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Work on {self.service_request} by {self.mechanic.get_name}"
