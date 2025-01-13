from django.urls import path
from .views import *

app_name = 'galery'

urlpatterns = [
    path('', galeries, name='galeries'),
]