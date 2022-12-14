# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alimento(models.Model):
    alim_id = models.AutoField(primary_key=True)
    alim_nombre = models.CharField(unique=True, max_length=80)
    alim_precio = models.DecimalField(max_digits=6, decimal_places=2)
    alim_categoria = models.CharField(max_length=12, blank=True, null=True)
    alim_comida_categoria = models.CharField(max_length=10, blank=True, null=True)
    alim_extras_categoria = models.CharField(max_length=7, blank=True, null=True)
    alim_bebida_categoria = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alimento'


class Carrito(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_alim = models.ForeignKey(Alimento, models.DO_NOTHING)
    car_alim_cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carrito'


class Orden(models.Model):
    ord_id = models.AutoField(primary_key=True)
    ord_num_alimentos = models.IntegerField()
    ord_fecha = models.DateField(blank=True, null=True)
    ord_estatus = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'


class OrdenAlimento(models.Model):
    ord_alim_id = models.AutoField(primary_key=True)
    ord_alim_alim = models.ForeignKey(Alimento, models.DO_NOTHING)
    ord_alim_ord = models.ForeignKey(Orden, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orden_alimento'
