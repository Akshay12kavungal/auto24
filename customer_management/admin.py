from django.contrib import admin
from .models import Customer, Notification, Vehicle, ServiceRequest, Feedback

from customer_management.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'mobile', 'address']
    search_fields = ['user__first_name', 'user__last_name', 'mobile', 'address']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'customer']
    search_fields = ['number', 'model', 'customer__user__first_name', 'customer__user__last_name']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['customer', 'vehicle', 'problem_description', 'status', 'cost', 'created_at']
    search_fields = ['customer__user__first_name', 'customer__user__last_name', 'vehicle__number', 'status']
    list_filter = ['status', 'created_at']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['customer', 'feedback', 'created_at']
    search_fields = ['customer__first_name', 'user__last_name', 'feedback']
    list_filter = ['created_at']
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('recipient__username', 'message')