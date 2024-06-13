from django.contrib import admin

from admin_management.models import AdminCommission

# Register your models here.


@admin.register(AdminCommission)
class AdminCommissionAdmin(admin.ModelAdmin):
    list_display = ['admin', 'amount', 'service_request', 'created_at']
    list_filter = ['admin', 'created_at']
    search_fields = ['admin__username', 'service_request__title']