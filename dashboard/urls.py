from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL pattern
    path('smart-lights/', views.smart_lights, name='smart_lights'),
    path('api/control-smart-switch/', views.control_smart_switch, name='control_smart_switch'),
    # Define other URL patterns as needed
]