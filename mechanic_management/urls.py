from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/mechanic/', views.signup_mechanic, name='signup_mechanic'),
    path('login_mechanic/', views.login_mechanic, name='login_mechanic'),
    path('mechanic/home/', views.mechanic_home, name='mechanic_home'),

    path('mechanic/profile/', views.view_mechanic_profile, name='view_mechanic_profile'),
    path('mechanic/update/profile/', views.update_mechanic_profile, name='update_mechanic_profile'),

    path('assigned-work/', views.assigned_work, name='assigned_work'),
    path('mechanic/work/update/<int:pk>/', views.update_work_status, name='update_work_status'),     
    path('mechanic/work/completed/', views.completed_work, name='completed_work'),
    path('earnings/', views.view_earnings, name='view_earnings'),
    
    path('logout/', views.mechanic_logout, name='mechanic_logout'),

#api
   path('api/mechanic/',include("mechanic_management.api.urls"))

]
