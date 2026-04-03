from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:pk>/', views.edit_student, name='edit'),
    path('delete/<int:pk>/', views.delete_student, name='delete'),
]