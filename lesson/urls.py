from django.urls import path
from .views import *

app_name = 'lesson'

urlpatterns = [
    path('', lessons, name='lessons'),
    path('<slug:lesson_slug>', lesson_detail, name='lesson_detail'),
]