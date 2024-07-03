from django.contrib import admin

from admin_management.models import AdminCommission
from .models import Booking, RentalCar


# Register your models here.


@admin.register(AdminCommission)
class AdminCommissionAdmin(admin.ModelAdmin):
    list_display = ['admin', 'amount', 'service_request', 'created_at']
    list_filter = ['admin', 'created_at']
    search_fields = ['admin__username', 'service_request__title']



@admin.register(RentalCar)
class RentalCarAdmin(admin.ModelAdmin):
    list_display = ['name', 'daily_rate', 'availability']
    list_filter = ['availability']
    search_fields = ['name', 'description']

    # Optional: Customize form fields displayed in the admin
    fieldsets = [
        (None, {'fields': ['name', 'description', 'image']}),
        ('Pricing', {'fields': ['daily_rate', 'availability']}),
    ]

    



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rental_car', 'user','start_date', 'end_date', 'total_price', 'status']
    list_filter = ['status','start_date', 'end_date']
    actions = ['accept_bookings', 'reject_bookings']

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'

    def accept_bookings(self, request, queryset):
        queryset.update(status=Booking.ACCEPTED)
    accept_bookings.short_description = "Accept selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status=Booking.REJECTED)
    reject_bookings.short_description = "Reject selected bookings"