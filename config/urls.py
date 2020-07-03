from django.contrib import admin
from django.urls import path, include

from appointments.api.urls import appointments_urls

admin.site.site_header = 'YEMA Test Christian Buendia Osorio'
admin.site.site_title = 'YEMA Test CBO'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(appointments_urls)),
]
