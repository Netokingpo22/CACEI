from django.db import models

class Maestro(models.Model):
    numeroProfesor = models.IntegerField()
    fechaIngreso = models.DateField()
    nombramientoActual = models.CharField(max_length=256)   

    def __str__(self):
        return f"id:{self.id} numero:{self.numeroProfesor} nombramiento:{self.nombramientoActual}" 
    
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
    evidencia = models.ImageField(upload_to='FormacionesAcademica/', null=True)

class CapacitacionDocente(models.Model):
    tipoCapacitacion = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    añoObtencion = models.DateField()
    horas = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='capacitacionDocente')
    evidencia = models.ImageField(upload_to='CapacitacionesDocente/', null=True)

class ActualizacionDisciplinar(models.Model):
    tipoActualizacion = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    añoObtencion = models.DateField()
    horas = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='actualizacionDisciplinar')
    evidencia = models.ImageField(upload_to='ActualizacionesDisciplinar/', null=True)

class GestionAcademica(models.Model):
    actividadPuesto = models.TextField(blank=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    inicio = models.DateField()
    fin = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='gestionAcademica')
    evidencia = models.ImageField(upload_to='GestionesAcademica/', null=True)

class ProductosAcademicosR(models.Model):
    nombre = models.CharField(max_length=256)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    fecha = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='productosAcademicosR')
    evidencia = models.ImageField(upload_to='ProductosAcademicosR/', null=True)

class ExpProfesionalNoA(models.Model):
    actividadPuesto = models.TextField(blank=False)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    inicio = models.DateField()
    fin = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='expProfesionalNoA')
    evidencia = models.ImageField(upload_to='ExpProfesionalesNoA/', null=True)

class ExpDiseñoIngenieril(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    periodo = models.DateField()
    nivel = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='expDiseñoIngenieril')
    evidencia = models.ImageField(upload_to='ExpDiseñoIngenieril/', null=True)

class LogrosProfesionalesNoA(models.Model):
    nombre = models.CharField(max_length=128)
    relevancia = models.CharField(max_length=128)
    autores = models.CharField(max_length=128)
    sede = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='logrosProfesionalesNoA')
    evidencia = models.ImageField(upload_to='LogrosProfesionalesNoA/', null=True)

class ParticipacionOrganismos(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    periodo = models.DateField()
    nivel = models.CharField(max_length=128)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='participacionOrganismos')
    evidencia = models.ImageField(upload_to='ParticipacionesOrganismos/', null=True)

class Reconocimientos(models.Model):
    nombre = models.CharField(max_length=128)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    fecha = models.DateField()
    extra = models.TextField(blank=True)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='reconocimientos')
    evidencia = models.ImageField(upload_to='Reconocimientos/', null=True)

class Aportacion(models.Model):
    descripcion = models.TextField(blank=False)
    maestro = models.ForeignKey(Maestro, on_delete=models.PROTECT, related_name='aportacion')
    evidencia = models.ImageField(upload_to='Aportaciones/', null=True)

