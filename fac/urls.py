from django.urls import path
from .views import ClienteView, ClienteNew, ClienteEdit


urlpatterns = [
    path('cliente/', ClienteView.as_view(), name='cliente_list'),
    path('cliente/new', ClienteNew.as_view(), name='cliente_new'),
    path('cliente/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
]