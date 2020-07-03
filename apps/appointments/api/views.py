from rest_framework.generics import CreateAPIView
from .serializers import AppointmentSerializer


class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentSerializer

