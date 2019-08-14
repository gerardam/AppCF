from django.shortcuts import render, redirect
from django.views import generic

from django.urls import reverse_lazy
#from django.contrib.messages.views import SuccessMessageMixin
    
from .models import Cliente
from .forms import ClienteForm
from bases.views import SinPrivilegios


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
    