from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def maestros(request):
    if request.method == 'GET':
        maestros = Maestro.objects.all()
        serializer = MaestroSerializer(maestros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaestroSerializer(data=request.data)
        if serializer.is_valid():
            maestro = serializer.save()
            return Response({"id": maestro.id, "numeroProfesor": maestro.numeroProfesor})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def instituciones(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            institucion = serializer.save()
            return Response({"id": institucion.id, "nombre": institucion.nombre})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def formaciones(request):
    if request.method == 'GET':
        formaciones = FormacionAcademica.objects.all()
        serializer = FormacionAcademicaSerializer(formaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FormacionAcademicaSerializer(data=request.data)
        if serializer.is_valid():
            formacion = serializer.save()
            return Response({"id": formacion.id, "nombre": formacion.nombre})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def capacitaciones(request):
    if request.method == 'GET':
        capacitaciones = CapacitacionDocente.objects.all()
        serializer = CapacitacionDocenteSerializer(capacitaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CapacitacionDocenteSerializer(data=request.data)
        if serializer.is_valid():
            capacitacion = serializer.save()
            return Response({"id": capacitacion.id, "tipoCapacitacion": capacitacion.tipoCapacitacion})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def actualizaciones(request):
    if request.method == 'GET':
        actualizaciones = ActualizacionDisciplinar.objects.all()
        serializer = ActualizacionDisciplinarSerializer(
            actualizaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActualizacionDisciplinarSerializer(data=request.data)
        if serializer.is_valid():
            actualizacion = serializer.save()
            return Response({"id": actualizacion.id, "tipoActualizacion": actualizacion.tipoActualizacion})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def gestiones(request):
    if request.method == 'GET':
        gestiones = GestionAcademica.objects.all()
        serializer = GestionAcademicaSerializer(gestiones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GestionAcademicaSerializer(data=request.data)
        if serializer.is_valid():
            gestion = serializer.save()
            return Response({"id": gestion.id, "actividadPuesto": gestion.actividadPuesto})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def productos(request):
    if request.method == 'GET':
        productos = ProductosAcademicosR.objects.all()
        serializer = ProductosAcademicosRSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductosAcademicosRSerializer(data=request.data)
        if serializer.is_valid():
            producto = serializer.save()
            return Response({"id": producto.id, "nombre": producto.nombre})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def exp_profesional_no_a(request):
    if request.method == 'GET':
        exp_profesional_no_a = ExpProfesionalNoA.objects.all()
        serializer = ExpProfesionalNoASerializer(
            exp_profesional_no_a, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExpProfesionalNoASerializer(data=request.data)
        if serializer.is_valid():
            exp_profesional_no_a = serializer.save()
            return Response({"id": exp_profesional_no_a.id, "actividadPuesto": exp_profesional_no_a.actividadPuesto})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def exp_diseño_ingenieril(request):
    if request.method == 'GET':
        exp_diseño_ingenieril = ExpDiseñoIngenieril.objects.all()
        serializer = ExpDiseñoIngenierilSerializer(
            exp_diseño_ingenieril, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExpDiseñoIngenierilSerializer(data=request.data)
        if serializer.is_valid():
            exp_diseño_ingenieril = serializer.save()
            return Response({"id": exp_diseño_ingenieril.id, "nivel": exp_diseño_ingenieril.nivel})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def logros_profesionales_no_a(request):
    if request.method == 'GET':
        logros_profesionales_no_a = LogrosProfesionalesNoA.objects.all()
        serializer = LogrosProfesionalesNoASerializer(
            logros_profesionales_no_a, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LogrosProfesionalesNoASerializer(data=request.data)
        if serializer.is_valid():
            logros_profesionales_no_a = serializer.save()
            return Response({"id": logros_profesionales_no_a.id, "nombre": logros_profesionales_no_a.nombre})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def participacion_organismos(request):
    if request.method == 'GET':
        participacion_organismos = ParticipacionOrganismos.objects.all()
        serializer = ParticipacionOrganismosSerializer(
            participacion_organismos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ParticipacionOrganismosSerializer(data=request.data)
        if serializer.is_valid():
            participacion_organismos = serializer.save()
            return Response({"id": participacion_organismos.id, "nivel": participacion_organismos.nivel})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reconocimientos(request):
    if request.method == 'GET':
        reconocimientos = Reconocimientos.objects.all()
        serializer = ReconocimientosSerializer(reconocimientos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReconocimientosSerializer(data=request.data)
        if serializer.is_valid():
            reconocimientos = serializer.save()
            return Response({"id": reconocimientos.id, "nombre": reconocimientos.nombre})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def aportacion(request):
    if request.method == 'GET':
        aportacion = Aportacion.objects.all()
        serializer = AportacionSerializer(aportacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AportacionSerializer(data=request.data)
        if serializer.is_valid():
            aportacion = serializer.save()
            return Response({"id": aportacion.id, "descripcion": aportacion.descripcion})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
