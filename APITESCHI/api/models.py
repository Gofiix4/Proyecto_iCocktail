from django.db import models

# Create your models here.
class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')
    class Meta:
        db_table='Generos'

class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True,db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
    class Meta:
        db_table='Alumnos'

class alumno_has_genero(models.Model):
    idalumno_has_genero = models.AutoField(primary_key=True,default=1,db_column='idalumno_has_genero')
    fk_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,db_column='fk_alumno')
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='alumno_has_genero'

class cocteles(models.Model):
    idCoctel = models.IntegerField(primary_key=True,db_column='idCoctel')
    Nombre = models.CharField(max_length=100,db_column='Nombre')
    Descripcion = models.CharField(max_length=500,db_column='Descripcion')
    imagen = models.CharField(max_length=250,db_column='imagen')
    class Meta:
        db_table='cocteles'

class ingredientes(models.Model):
    idIngrediente = models.IntegerField(primary_key=True,db_column='idIngrediente')
    Nombre = models.CharField(max_length=50,db_column='Nombre')
    Descripcion = models.CharField(max_length=500,db_column='Descripcion')
    class Meta:
        db_table='ingredientes'

class recetas(models.Model):
    idReceta = models.IntegerField(primary_key=True,db_column='idReceta')
    fk_idCoctel = models.ForeignKey(cocteles,on_delete=models.CASCADE,db_column='fk_idCocteles')
    fk_idIngrediente = models.ForeignKey(ingredientes,on_delete=models.CASCADE,db_column='fk_idIngredientes')
    cantidad = models.CharField(max_length=10,db_column='Cantidad')
    instrucciones = models.CharField(max_length=200,db_column='Instrucciones')
    class Meta:
        db_table='recetas'

