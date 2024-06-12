from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('signup/mechanic/', views.signup_mechanic, name='signup_mechanic'),
    path('login_customer/', views.login_customer, name='login_customer'),
    path('login_mechanic/', views.login_mechanic, name='login_mechanic'),
    path('login_admin/', views.admin_login, name='login_admin'),

    path('logout/', views.user_logout, name='user_logout'),
    path('logout/', views.mechanic_logout, name='mechanic_logout'),
    
    path('customer/home/', views.customer_home, name='customer_home'),
    path('edit-customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('fill-vehicle-details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('customer/service-request/', views.make_service_request, name='make_service_request'),
    path('customer/service-request/delete/<int:pk>/', views.delete_service_request, name='delete_service_request'),
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    path('customer/feedback/', views.customer_feedback, name='customer_feedback'),

    path('mechanic/home/', views.mechanic_home, name='mechanic_home'),
    path('assigned-work/', views.assigned_work, name='assigned_work'),
    path('edit-mechanic/<int:pk>/', views.edit_mechanic, name='edit_mechanic'),
    path('delete-mechanic/<int:pk>/', views.delete_mechanic, name='delete_mechanic'),
    path('mechanic/profile/', views.mechanic_profile, name='mechanic_profile'),
    path('mechanic/feedback/', views.mechanic_feedback, name='mechanic_feedback'),
    path('mechanic/work/update/<int:pk>/', views.update_work_status, name='update_work_status'),

    path('adminpage/home/', views.admin_home, name='admin_home'),
    path('adminpage/manage-customers/', views.manage_customers, name='manage_customers'),
    path('adminpage/manage-mechanics/', views.manage_mechanics, name='manage_mechanics'),
    path('adminpage/approve-mechanic/<int:pk>/', views.approve_mechanic, name='approve_mechanic'),
    path('adminpage/manage-service-requests/', views.manage_service_requests, name='manage_service_requests'),
    path('adminpage/approve-service-request/<int:pk>/', views.approve_service_request, name='approve_service_request'),
    path('adminpage/assign-mechanic/<int:pk>/', views.assign_mechanic, name='assign_mechanic'),
    path('logout/', views.admin_logout, name='admin_logout'),
   

]

