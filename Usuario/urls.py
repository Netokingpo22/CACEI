from django.urls import path
from Usuario.views import registrar

urlpatterns = [
    path('registrar', registrar, name='usuario_api'),
]
