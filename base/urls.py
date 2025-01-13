from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('hakkımızda/', about, name='about'),
    path('error/', error, name='error'),
]