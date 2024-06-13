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
