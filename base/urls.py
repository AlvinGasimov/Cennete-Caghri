from django.urls import path
from .views import index, about, contact, error, galeries

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('hakkimizda/', about, name='about'),
    path('galeri/', galeries, name='galeries'),
    path('iletisim/', contact, name='contact'),
    path('error/', error, name='error'),
]