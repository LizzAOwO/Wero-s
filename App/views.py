from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.db.models import Subquery
from django.core import serializers
from App.models import Alimento, Carrito, Orden, OrdenAlimento
import datetime

# Create your views here.
def home(request):
    data = serializers.serialize("json", Alimento.objects.all())
    return render(request,"index.html", {"data":data})

def carrito_add(request):
    data = request.POST
    if Carrito.objects.filter(car_alim = data['id']).exists():
        for up in Carrito.objects.prefetch_related('car_alim').filter(car_alim = data['id']):
            up.car_alim_cantidad += int(data["cantidad"])
            if up.car_alim.alim_categoria == 'Extra' and up.car_alim_cantidad > 10:
                up.car_alim_cantidad = 10
            up.save()
    else:
        Carrito.objects.create(car_alim = Alimento(alim_id=data['id']), car_alim_cantidad = data['cantidad'])
    return redirect("/")

def carrito(request):
    data =  Carrito.objects.prefetch_related('car_alim')
    total = 0
    for i in data:
        total += i.car_alim_cantidad * i.car_alim.alim_precio
    return render(request,"carrito.html",{"data":data, "total": total})

def carrito_del(request, id):
    Carrito.objects.filter(car_id = id).delete()
    return redirect("/carrito")

def pago(request):
    data =  Carrito.objects.prefetch_related('car_alim')
    total = 0
    for i in data:
        total += i.car_alim_cantidad * i.car_alim.alim_precio
    data =  Carrito.objects.prefetch_related('car_alim')

    return render(request,"pagos.html",{"data":data, "total": total})

def pago_aceptar(request):
    data = request.POST
    car = Carrito.objects.prefetch_related('car_alim')
    ord = Orden.objects.create(ord_nombre = data['nombre'],
                                ord_tel = data['telefono'],
                                ord_dir = data['direccion'],
                                ord_cp = data['cp'],
                                ord_fecha = datetime.datetime.now().date(),
                                ord_total = data['total'],
                                ord_estatus = "En preparacion")
    for c in car:
        OrdenAlimento.objects.create(ord_alim_alim = Alimento(alim_id=c.car_alim.alim_id),
                                     ord_alim_ord = Orden(ord_id = ord.ord_id), 
                                     ord_alim_cantidad = c.car_alim_cantidad)
        c.delete()
    return redirect("/")

def pedidos(request):
    orden = Orden.objects.all().order_by('ord_fecha')
    alimentos = OrdenAlimento.objects.prefetch_related('ord_alim_ord', 'ord_alim_alim')
    return render(request, "pedidos.html",{"ord":orden, "alim": alimentos})