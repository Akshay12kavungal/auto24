from django.urls import include, path
from . import views
import customer_management

urlpatterns = [
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('login_customer/', views.login_customer, name='login_customer'),

    path('customer/home/', views.customer_home, name='customer_home'),
    path('customer/profile/', views.view_customer_profile, name='view_customer_profile'),
    path('customer/update/profile/', views.update_customer_profile, name='update_customer_profile'),

    path('fill-vehicle-details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('customer/service-request/', views.make_service_request, name='make_service_request'),
    path('service-request/<int:pk>/', views.service_request_detail, name='service_request_detail'),
    
    path('customer/service-request/delete/<int:pk>/', views.delete_service_request, name='delete_service_request'),
    path('customer/feedback/', views.customer_feedback, name='customer_feedback'),
    path('customer/booking-history/', views.booking_history, name='booking_history'),

    path('list/', views.notification_list, name='notification_list'),
   

    path('logout/', views.user_logout, name='user_logout'),

#api

    path('api/customer/',include("customer_management.api.urls"))
]
