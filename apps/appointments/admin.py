from django.contrib import admin

from .models import Appointment


class AppointmentInline(admin.TabularInline):
    extra = 0
    model = Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'pediatrician', 'date')
    list_filter = ('pediatrician', 'date')
    search_fields = ('user__email', 'pediatrician__user__email')

