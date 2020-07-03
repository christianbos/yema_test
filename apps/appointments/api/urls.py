from django.urls import path
from .views import AppointmentCreateView


appointments_urls = [
    path('appointments', AppointmentCreateView.as_view(), name='appointments'),
]
