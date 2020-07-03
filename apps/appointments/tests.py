from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AppointmentCreateTest(APITestCase):
    def test_create_appointment(self):
        """
            Ensure we can create a new appointment object
        """
        url = reverse('appointments')
        data = {
            'user': 1,
            'pediatrician': 1,
            'comment': 'Necesito una cita urgente',
            'date': str(timezone.now())
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

