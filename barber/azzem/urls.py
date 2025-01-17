from django.urls import path
from .views import home, process_booking

urlpatterns = [
    path('', home, name='home'),
    path('booking/', process_booking, name='booking')
]
