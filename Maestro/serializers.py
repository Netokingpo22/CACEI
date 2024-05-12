from rest_framework import serializers
from .models import *


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


class FormacionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacionAcademica
        fields = '__all__'


class CapacitacionDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapacitacionDocente
        fields = '__all__'


class ActualizacionDisciplinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActualizacionDisciplinar
        fields = '__all__'


class GestionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionAcademica
        fields = '__all__'


class ProductosAcademicosRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosAcademicosR
        fields = '__all__'


class ExpProfesionalNoASerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpProfesionalNoA
        fields = '__all__'


class ExpDiseñoIngenierilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpDiseñoIngenieril
        fields = '__all__'


class LogrosProfesionalesNoASerializer(serializers.ModelSerializer):
    class Meta:
        model = LogrosProfesionalesNoA
        fields = '__all__'


class ParticipacionOrganismosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipacionOrganismos
        fields = '__all__'


class ReconocimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reconocimientos
        fields = '__all__'


class AportacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aportacion
        fields = '__all__'


class MaestroSerializer(serializers.ModelSerializer):
    formacionAcademica = FormacionAcademicaSerializer(
        many=True, read_only=True)
    capacitacionDocente = CapacitacionDocenteSerializer(
        many=True, read_only=True)
    actualizacionDisciplinar = ActualizacionDisciplinarSerializer(
        many=True, read_only=True)
    gestionAcademica = GestionAcademicaSerializer(many=True, read_only=True)
    productosAcademicosR = ProductosAcademicosRSerializer(
        many=True, read_only=True)
    expProfesionalNoA = ExpProfesionalNoASerializer(many=True, read_only=True)
    expDiseñoIngenieril = ExpDiseñoIngenierilSerializer(
        many=True, read_only=True)
    logrosProfesionalesNoA = LogrosProfesionalesNoASerializer(
        many=True, read_only=True)
    participacionOrganismos = ParticipacionOrganismosSerializer(
        many=True, read_only=True)
    reconocimientos = ReconocimientosSerializer(many=True, read_only=True)
    aportacion = AportacionSerializer(many=True, read_only=True)

    class Meta:
        model = Maestro
        fields = '__all__'
