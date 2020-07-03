from django.contrib import admin

from .models import User, Pediatrician
from appointments.admin import AppointmentInline


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'id')


@admin.register(Pediatrician)
class PediatricianAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')
    inlines = [AppointmentInline, ]

