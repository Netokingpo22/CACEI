from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Maestro, Institucion, FormacionAcademica
from .serializers import MaestroSerializer, InstitucionSerializer, FormacionAcademicaSerializer

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
