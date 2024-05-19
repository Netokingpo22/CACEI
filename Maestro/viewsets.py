from rest_framework import viewsets
from Maestro.models import *
from Maestro.serializers import *

class MaestroViewSet(viewsets.ModelViewSet):
	queryset = Maestro.objects.all()
	serializer_class = MaestroSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class FormacionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = FormacionAcademica.objects.all()
    serializer_class = FormacionAcademicaSerializer

class CapacitacionDocenteViewSet(viewsets.ModelViewSet):
    queryset = CapacitacionDocente.objects.all()
    serializer_class = CapacitacionDocenteSerializer

class ActualizacionDisciplinarViewSet(viewsets.ModelViewSet):
    queryset = ActualizacionDisciplinar.objects.all()
    serializer_class = ActualizacionDisciplinarSerializer

class GestionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = GestionAcademica.objects.all()
    serializer_class = GestionAcademicaSerializer

class ProductosAcademicosRViewSet(viewsets.ModelViewSet):
    queryset = ProductosAcademicosR.objects.all()
    serializer_class = ProductosAcademicosRSerializer

class ExpProfesionalNoAViewSet(viewsets.ModelViewSet):
    queryset = ExpProfesionalNoA.objects.all()
    serializer_class = ExpProfesionalNoASerializer

class ExpDiseñoIngenierilViewSet(viewsets.ModelViewSet):
    queryset = ExpDiseñoIngenieril.objects.all()
    serializer_class = ExpDiseñoIngenierilSerializer

class LogrosProfesionalesNoAViewSet(viewsets.ModelViewSet):
    queryset = LogrosProfesionalesNoA.objects.all()
    serializer_class = LogrosProfesionalesNoASerializer

class ParticipacionOrganismosViewSet(viewsets.ModelViewSet):
    queryset = ParticipacionOrganismos.objects.all()
    serializer_class = ParticipacionOrganismosSerializer

class ReconocimientosViewSet(viewsets.ModelViewSet):
    queryset = Reconocimientos.objects.all()
    serializer_class = ReconocimientosSerializer

class AportacionViewSet(viewsets.ModelViewSet):
    queryset = Aportacion.objects.all()
    serializer_class = AportacionSerializer
