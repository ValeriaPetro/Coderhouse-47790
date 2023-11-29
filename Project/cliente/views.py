from django.shortcuts import render

from . import models

from datetime import date

def home (request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def crear_clientes_varios(request):
    p1 = models.pais(nombre="Peru")
    p2 = models.pais(nombre="Mexico")
    p3 = models.pais(nombre="El Salvador")
    p1.save()
    p2.save()
    p3.save()
    c1 = models.Cliente(nombre="Almendra", apellido="Ruisenior", nacimiento=date(2015,1,1), pais_origen=p1)
    c2 = models.Cliente(nombre="Giordana", apellido="Tapello", nacimiento=date(2005,2,2), pais_origen=p2)
    
    