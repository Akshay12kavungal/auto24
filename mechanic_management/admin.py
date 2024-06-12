from django.contrib import admin
from .models import Mechanic, MechanicWork

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