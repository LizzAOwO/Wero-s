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
    ord_fecha = models.DateField(blank=True, null=True)
    ord_estatus = models.CharField(max_length=14, blank=True, null=True)
    ord_nombre = models.CharField(max_length=45, blank=True, null = True)
    ord_tel = models.CharField(max_length=10, blank=True, null = True)
    ord_dir = models.CharField(max_length=100, blank=True, null = True)
    ord_cp = models.CharField(max_length=10, blank=True, null = True)
    ord_total = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'orden'


class OrdenAlimento(models.Model):
    ord_alim_id = models.AutoField(primary_key=True)
    ord_alim_alim = models.ForeignKey(Alimento, models.DO_NOTHING)
    ord_alim_ord = models.ForeignKey(Orden, models.DO_NOTHING)
    ord_alim_cantidad = models.IntegerField(null = False)
    class Meta:
        managed = False
        db_table = 'orden_alimento'