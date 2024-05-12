from django.db import models


class Maestro(models.Model):
    numeroProfesor = models.IntegerField()
    fechaIngreso = models.DateField()
    nombramientoActual = models.CharField(max_length=256)
    
class Institucion(models.Model):
    nombre = models.CharField(max_length=256)
    siglas = models.CharField(max_length=32)
    pais = models.CharField(max_length=128)

Nivel = {
    'Licenciatura': 'Licenciatura',
    'Especialización': 'Especialización',
    'Maestria': 'Maestria',
    'Doctorado': 'Doctorado',
}

class FormacionAcademica(models.Model):
    nivel = models.CharField(max_length=64, choices=Nivel.items())
    nombre = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    añoObtencion = models.DateField()
    cedulaProfesional = models.CharField(max_length=256)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='formacionAcademica')

class CapacitacionDocente(models.Model):
    tipoCapacitacion = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    añoObtencion = models.DateField()
    horas = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='capacitacionDocente')

class ActualizacionDisciplinar(models.Model):
    tipoActualizacion = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    añoObtencion = models.DateField()
    horas = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='actualizacionDisciplinar')

class GestionAcademica(models.Model):
    actividadPuesto = models.TextField(blank=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    inicio = models.DateField()
    fin = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='gestionAcademica')

class ProductosAcademicosR(models.Model):
    nombre = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    fecha = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='productosAcademicosR')

class ExpProfesionalNoA(models.Model):
    actividadPuesto = models.TextField(blank=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    inicio = models.DateField()
    fin = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='expProfesionalNoA')

class ExpDiseñoIngenieril(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    periodo = models.DateField()
    nivel = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='expDiseñoIngenieril')

class LogrosProfesionalesNoA(models.Model):
    nombre = models.CharField(max_length=128)
    relevancia = models.CharField(max_length=128)
    autores = models.CharField(max_length=128)
    sede = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='logrosProfesionalesNoA')

class ParticipacionOrganismos(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    periodo = models.DateField()
    nivel = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='participacionOrganismos')

class Reconocimientos(models.Model):
    nombre = models.CharField(max_length=128)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    fecha = models.DateField()
    extra = models.TextField(blank=True)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='reconocimientos')

class Aportacion(models.Model):
    descripcion = models.TextField(blank=False)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='aportacion')

