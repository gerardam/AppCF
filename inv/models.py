from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).Save()

    class Meta:
        verbose_name_plural = 'Categorías'


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).Save()

    class Meta:
        verbose_name_plural = 'Subcategorías'
        unique_together = ('categoria', 'descripcion')
        

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).Save()

    class Meta:
        verbose_name_plural = 'Marcas'


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la unidad de medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).Save()

    class Meta:
        verbose_name_plural = 'Unidades de medida'
