from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.db.models import Subquery
from django.core import serializers
from App.models import Alimento, Carrito, Orden, OrdenAlimento

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
    return render(request,"Pagos.html")