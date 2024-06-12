from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name

class Vehicle(models.Model):
    number = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.model} ({self.number})"

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Repairing Done', 'Repairing Done'),
        ('Work Done', 'Work Done')

    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_requests')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='service_requests')
    problem_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Service Request for {self.vehicle} by {self.customer.get_name}"

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='feedbacks')
    mechanic = models.ForeignKey('mechanic_management.Mechanic', on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.customer.get_name} for {self.mechanic.get_name}"
