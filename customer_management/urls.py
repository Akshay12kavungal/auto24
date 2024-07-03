from django.urls import include, path
from . import views
import customer_management

urlpatterns = [
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('login_customer/', views.login_customer, name='login_customer'),
    path('logout/', views.user_logout, name='user_logout'),


    path('customer/home/', views.customer_home, name='customer_home'),
    path('customer/profile/', views.view_customer_profile, name='view_customer_profile'),
    path('customer/update/profile/', views.update_customer_profile, name='update_customer_profile'),

    path('fill-vehicle-details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('customer/service-request/', views.make_service_request, name='make_service_request'),
    path('service-request/<int:pk>/', views.service_request_detail, name='service_request_detail'),

    
    path('customer/feedback/', views.customer_feedback, name='customer_feedback'),
    path('customer/booking-history/', views.booking_history, name='booking_history'),
    path('customer/list/', views.notification_list, name='notification_list'),
   

    path('customer/rental-cars/', views.rental_car_list, name='customer_rental_car_list'),
    path('book-car/<int:car_id>/', views.book_car, name='book_car'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booking/', views.booking_list, name='booking_list'),
    path('booking/update/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),

    


#api

    path('api/customer/',include("customer_management.api.urls"))
]
