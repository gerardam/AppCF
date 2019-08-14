from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,\
    PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Cliente
# from .forms import ClienteForm
from bases.views import SinPrivilegios


########## CLIENTES ##########
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = 'fac.view_cliente'
    model = Cliente
    template_name = 'fac/cliente_list.html'
    context_object_name = 'obj'

# class ClienteNew(SinPrivilegios, generic.CreateView):
#     permission_required = 'fac.add_cliente'
#     model = Cliente
#     template_name = 'fac/cliente_form.html'
#     context_object_name = 'obj'
#     form_class = ClienteForm
#     success_url = reverse_lazy('fac:cliente_list')

#     def form_valid(self, form):
#         form.instance.uc = self.request.user
#         return super().form_valid(form)

# class ClienteEdit(SinPrivilegios, generic.UpdateView):
#     permission_required = 'fac.change_cliente'
#     model = Cliente
#     template_name = 'fac/cliente_form.html'
#     context_object_name = 'obj'
#     form_class = ClienteForm
#     success_url = reverse_lazy('fac:cliente_list')

#     def form_valid(self, form):
#         form.instance.um = self.request.user.id
#         return super().form_valid(form)

