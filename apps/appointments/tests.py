from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import User, Pediatrician


class AppointmentCreateTest(APITestCase):
    def test_create_appointment(self):
        """
            Ensure we can create a new appointment object
        """
        user = User.objects.create_user(
                'christianbos91@gmail.com',
                'contraseña',
                first_name='Christian',
                last_name='Buendia'
            )
        user2 = User.objects.create_user(
                'test@gmail.com',
                'contraseña',
                first_name='Brenda',
                last_name='Buendia',
                is_pediatrician=True
        )
        pediatrician = Pediatrician.objects.create(
            user=user2,
            professional_licence='1341adf1f',
            university='UVM'
        )
        url = reverse('appointments')
        data = {
            'user': user.pk,
            'pediatrician': pediatrician.pk,
            'comment': 'Necesito una cita urgente',
            'date': str(timezone.now())
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

