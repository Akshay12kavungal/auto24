
from django.urls import include, path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('adminpage/home/', views.admin_home, name='admin_home'),
    path('adminpage/manage-customers/', views.manage_customers, name='manage_customers'),
    path('adminpage/manage-mechanics/', views.manage_mechanics, name='manage_mechanics'),
    path('adminpage/approve-mechanic/<int:pk>/', views.approve_mechanic, name='approve_mechanic'),
    path('adminpage/manage-service-requests/', views.manage_service_requests, name='manage_service_requests'),
    path('adminpage/approve-service-request/<int:pk>/', views.approve_service_request, name='approve_service_request'),
    path('adminpage/assign-mechanic/<int:pk>/', views.assign_mechanic, name='assign_mechanic'),
    path('logout/', views.admin_logout, name='admin_logout'),
   
#customer crud
    path('edit-customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),  

#mechanic crud
    path('edit-mechanic/<int:pk>/', views.edit_mechanic, name='edit_mechanic'),
    path('delete-mechanic/<int:pk>/', views.delete_mechanic, name='delete_mechanic'),


#rental car

    path('adminpage/rental-cars/', views.rental_car_list, name='rental_car_list'),
    path('adminpage/add-rental-car/', views.add_rental_car, name='add_rental_car'),
    path('adminpage/edit-rental-car/<int:pk>/', views.edit_rental_car, name='edit_rental_car'),
    path('adminpage/delete-rental-car/<int:pk>/', views.delete_rental_car, name='delete_rental_car'),

#api
    path("api/admin/", include("admin_management.api.urls")),
]