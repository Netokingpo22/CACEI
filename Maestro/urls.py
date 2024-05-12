from django.urls import path
from .views import *

urlpatterns = [
    path('maestros/', maestros, name='maestros'),
    path('instituciones/', instituciones, name='instituciones'),
    path('formaciones/', formaciones, name='formaciones'),
]
