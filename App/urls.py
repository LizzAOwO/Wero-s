from django.urls import path
from App import views

urlpatterns = [
    path('',views.home),
    path('carrito', views.carrito),
    path('carrito-add', views.carrito_add),
    path('carrito_del/<int:id>', views.carrito_del),
    path('pago', views.pago),
]