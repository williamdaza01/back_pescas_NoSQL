from django.db import models

# Create your models here.
class Cuenca(models.Model):
    ID_CUENCA = models.IntegerField(db_column='ID_CUENCA', blank=True)  # Field name made lowercase.
    NOMBRE_CUENCA = models.TextField(unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuenca'


class Metodo(models.Model):
    ID_METODO = models.IntegerField(db_column='ID_METODO', blank=True)  # Field name made lowercase.
    NOMBRE_METODO = models.TextField(unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metodo'


class Pesca(models.Model):
    ID_PESCA = models.IntegerField(blank=True)  # Field name made lowercase.
    ID_CUENCA = models.ForeignKey(Cuenca, models.DO_NOTHING, db_column='ID_CUENCA')  # Field name made lowercase.
    ID_METODO = models.ForeignKey(Metodo, models.DO_NOTHING, db_column='ID_METODO')  # Field name made lowercase.
    FECHA_PESCA = models.TextField(db_column='FECHA_PESCA')  # Field name made lowercase.
    PESO_PESCADO = models.TextField(db_column='PESO_PESCADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pesca'