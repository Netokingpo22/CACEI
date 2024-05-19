from .views import *
from rest_framework import routers
from Maestro.viewsets import *

route = routers.SimpleRouter()
route.register('maestro', MaestroViewSet)
route.register('institucion', InstitucionViewSet)
route.register('formacion', FormacionAcademicaViewSet)
route.register('capacitacion', CapacitacionDocenteViewSet)
route.register('disciplinar', ActualizacionDisciplinarViewSet)
route.register('gestion', GestionAcademicaViewSet)
route.register('productos', ProductosAcademicosRViewSet)
route.register('expNoAcademica', ExpProfesionalNoAViewSet)
route.register('expIngenieril', ExpDiseñoIngenierilViewSet)
route.register('logrosNoAcademicos', LogrosProfesionalesNoAViewSet)
route.register('participacion', ParticipacionOrganismosViewSet)
route.register('reconocimientos', ReconocimientosViewSet)
route.register('aportacion', AportacionViewSet)
urlpatterns = route.urls
