from django.contrib import admin
from .models import Mechanic, MechanicEarnings, MechanicWork

@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'mobile', 'address', 'skill', 'salary', 'status']
    search_fields = ['user__first_name', 'user__last_name', 'mobile', 'address', 'skills']
    list_filter = ['status']

@admin.register(MechanicWork)
class MechanicWorkAdmin(admin.ModelAdmin):
    list_display = ['mechanic', 'service_request', 'status', 'assigned_at']
    search_fields = ['mechanic__user__first_name', 'mechanic__user__last_name', 'service_request__vehicle__number']
    list_filter = ['status', 'assigned_at']



@admin.register(MechanicEarnings)
class MechanicEarningsAdmin(admin.ModelAdmin):
    list_display = ['mechanic', 'amount', 'service_request', 'created_at']
    list_filter = ['mechanic', 'created_at']
    search_fields = ['mechanic__username', 'service_request__title']