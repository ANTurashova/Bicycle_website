from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prod/', views.prod, name='prod'),
]