# Generated by Django 4.2.5 on 2024-05-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maestro', '0002_formacionacademica_evidencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualizaciondisciplinar',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='ActualizacionesDisciplinar/'),
        ),
        migrations.AddField(
            model_name='aportacion',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='Aportaciones/'),
        ),
        migrations.AddField(
            model_name='capacitaciondocente',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='CapacitacionesDocente/'),
        ),
        migrations.AddField(
            model_name='expdiseñoingenieril',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='ExpDiseñoIngenieril/'),
        ),
        migrations.AddField(
            model_name='expprofesionalnoa',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='ExpProfesionalesNoA/'),
        ),
        migrations.AddField(
            model_name='gestionacademica',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='GestionesAcademica/'),
        ),
        migrations.AddField(
            model_name='logrosprofesionalesnoa',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='LogrosProfesionalesNoA/'),
        ),
        migrations.AddField(
            model_name='participacionorganismos',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='ParticipacionesOrganismos/'),
        ),
        migrations.AddField(
            model_name='productosacademicosr',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='ProductosAcademicosR/'),
        ),
        migrations.AddField(
            model_name='reconocimientos',
            name='evidencia',
            field=models.ImageField(null=True, upload_to='Reconocimientos/'),
        ),
    ]