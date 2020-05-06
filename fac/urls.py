from django.urls import path, include
from .views import ClienteView, ClienteNew, ClienteEdit, ClienteInactivar, \
FacturaView, facturas, ProductoView


urlpatterns = [
    path('cliente/', ClienteView.as_view(), name='cliente_list'),
    path('cliente/new', ClienteNew.as_view(), name='cliente_new'),
    path('cliente/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('cliente/estado/<int:id>', ClienteInactivar, name='cliente_inactivar'),

    path('factura/', FacturaView.as_view(), name='factura_list'),
    path('factura/new', facturas, name='factura_new'),
    path('factura/buscar-producto', ProductoView.as_view(), name='factura_producto'),
]