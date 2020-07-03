from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Correo eletrónico'
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Nombre'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Apellidos'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha registro'
    )
    photo = models.ImageField(
        upload_to='avatars/',
        max_length=300,
        blank=True,
        null=True,
    )
    is_pediatrician = models.BooleanField(
        default=False,
        verbose_name="Es pediatra"
    )
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    is_staff = models.BooleanField(default=False, verbose_name='Es Staff')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class Pediatrician(models.Model):
    user = models.OneToOneField(
        User,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    professional_licence = models.CharField(
        max_length=30,
        blank=False,
        verbose_name='Cédula profesional',
    )
    university = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Universidad'
    )

    class Meta:
        verbose_name = 'Pediatra'

    def __str__(self):
        return self.user.get_full_name()


