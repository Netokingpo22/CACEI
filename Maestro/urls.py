from django.urls import path
from .views import *

urlpatterns = [
    path('maestros/', maestros, name='maestros'),
    path('instituciones/', instituciones, name='instituciones'),
    path('formaciones/', formaciones, name='formaciones'),
    path('capacitaciones/', capacitaciones, name='capacitaciones'),
    path('actualizaciones/', actualizaciones, name='actualizaciones'),
    path('gestiones/', gestiones, name='gestiones'),
    path('productos/', productos, name='productos'),
    path('exp_profesional_no_a/', exp_profesional_no_a, name='exp_profesional_no_a'),
    path('exp_diseño_ingenieril/', exp_diseño_ingenieril, name='exp_diseño_ingenieril'),
    path('logros_profesionales_no_a/', logros_profesionales_no_a, name='logros_profesionales_no_a'),
    path('participacion_organismos/', participacion_organismos, name='participacion_organismos'),
    path('reconocimientos/', reconocimientos, name='reconocimientos'),
    path('aportacion/', aportacion, name='aportacion'),
]
