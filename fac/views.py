from django.shortcuts import render, redirect
from django.views import generic

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime
    
from .models import Cliente, FacturaEnc, FacturaDet
from .forms import ClienteForm
from bases.views import SinPrivilegios


########## VISTAS BASE ##########
class VistaBaseCreate(SinPrivilegios, generic.CreateView):
    context_object_name = 'obj'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SinPrivilegios, generic.UpdateView):
    context_object_name = 'obj'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


########## CLIENTES ##########
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = 'fac.view_cliente'
    model = Cliente
    template_name = 'fac/cliente_list.html'
    context_object_name = 'obj'

class ClienteNew(VistaBaseCreate):
    permission_required = 'fac.add_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')

class ClienteEdit(VistaBaseEdit):
    permission_required = 'fac.change_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    
@login_required(login_url='/login/')
@permission_required('fac.change_cliente', login_url='bases:sin_privilegios')
def ClienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse('OK')
        return HttpResponse('FAIL')

    return HttpResponse('FAIL')


########## FACTURAS ##########
class FacturaView(SinPrivilegios, generic.ListView):
    permission_required = 'fac.view_facturaenc'
    model = FacturaEnc
    template_name = 'fac/factura_list.html'
    context_object_name = 'obj'

@login_required(login_url='/login/')
@permission_required('fac.change_facturasenc', login_url='bases:sin_privilegios')
def facturas(request,id=None):
    template_name = 'fac/facturas.html'

    encabezado = {
        'fecha':datetime.today()
    }
    detalle = {}
    clientes = Cliente.objects.filter(estado=True)
    

    contexto = {}

    return render (request, template_name, contexto)