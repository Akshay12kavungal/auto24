from django.db import models
from django.contrib.auth.models import User
from customer_management.models import ServiceRequest


class AdminCommission(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='commissions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commission earned by {self.admin.username} - ${self.amount}"



class RentalCar(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='rental_cars/')
    daily_rate=models.DecimalField(max_digits=10,decimal_places=2)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    rental_car = models.ForeignKey(RentalCar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.rental_car.name} - {self.user.username}"

    @property
    def total_price(self):
        duration = (self.end_date - self.start_date).days + 1
        return duration * self.rental_car.daily_rate

    
