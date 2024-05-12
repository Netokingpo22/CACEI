from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer


@api_view(['GET','POST'])
def registrar(request):
    if request.method == 'POST':
        username = request.data.get('username')
        if Usuario.objects.filter(username=username).exists():
            return Response({"detail": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({"id": usuario.id, "username": usuario.username})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)