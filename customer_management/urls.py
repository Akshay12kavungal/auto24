from django.urls import path
from . import views

urlpatterns = [
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('login_customer/', views.login_customer, name='login_customer'),
    path('customer/home/', views.customer_home, name='customer_home'),
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    path('fill-vehicle-details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('customer/service-request/', views.make_service_request, name='make_service_request'),
    path('customer/service-request/delete/<int:pk>/', views.delete_service_request, name='delete_service_request'),
    path('customer/feedback/', views.customer_feedback, name='customer_feedback'),
    path('logout/', views.user_logout, name='user_logout'),


]
