from django.urls import path
from . import views

urlpatterns = [
    path('signup/mechanic/', views.signup_mechanic, name='signup_mechanic'),
    path('login_mechanic/', views.login_mechanic, name='login_mechanic'),
    path('mechanic/home/', views.mechanic_home, name='mechanic_home'),
    path('mechanic/profile/', views.mechanic_profile, name='mechanic_profile'),
    path('assigned-work/', views.assigned_work, name='assigned_work'),
    path('mechanic/work/update/<int:pk>/', views.update_work_status, name='update_work_status'),
    path('logout/', views.mechanic_logout, name='mechanic_logout'),

]
