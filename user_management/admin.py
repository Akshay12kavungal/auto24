from django.contrib import admin
from .models import Customer, Mechanic, Vehicle, ServiceRequest, Invoice, Feedback, MechanicWork

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'mobile', 'address']
    search_fields = ['user__first_name', 'user__last_name', 'mobile', 'address']

class MechanicAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'mobile', 'address', 'skill', 'salary', 'status']
    search_fields = ['user__first_name', 'user__last_name', 'mobile', 'address', 'skills']
    list_filter = ['status']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'customer']
    search_fields = ['number', 'model', 'customer__user__first_name', 'customer__user__last_name']

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['customer', 'vehicle', 'problem_description', 'status', 'cost', 'created_at']
    search_fields = ['customer__user__first_name', 'customer__user__last_name', 'vehicle__number', 'status']
    list_filter = ['status', 'created_at']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['service_request', 'total_cost', 'created_at']
    search_fields = ['service_request__customer__user__first_name', 'service_request__customer__user__last_name']
    list_filter = ['created_at']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'feedback', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'feedback']
    list_filter = ['created_at']

class MechanicWorkAdmin(admin.ModelAdmin):
    list_display = ['mechanic', 'service_request', 'status', 'assigned_at']
    search_fields = ['mechanic__user__first_name', 'mechanic__user__last_name', 'service_request__vehicle__number']
    list_filter = ['status', 'assigned_at']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Mechanic, MechanicAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(MechanicWork, MechanicWorkAdmin)
