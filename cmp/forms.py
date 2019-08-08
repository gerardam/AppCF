from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)
    class Meta:
        model = Proveedor
        fields = ['descripcion','direccion','contacto','telefono','email',             'estado']
        exclude = ['um', 'fm','uc','fc']
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })