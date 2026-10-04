from django.urls import path

from .views import about, contact, index


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='saytlar_haqida'),
    path('contact/', contact, name='contact'),
]
