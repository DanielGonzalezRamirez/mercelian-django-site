from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('daniel/', views.daniel, name='daniel'),
    path('paula/', views.paula, name='paula'),
]