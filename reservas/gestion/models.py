from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)

    class Meta:
        #sirve para modificar alguna configuracion de la tabla de nuestra id
        db_table = 'categorias'