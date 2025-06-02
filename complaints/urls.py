from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('update/<int:complaint_id>/', views.update_status, name='update_status'),
    path('complaint/delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
]
