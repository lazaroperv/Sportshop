from django.db import models
# Create your models here.
class Productos(models.Model):
            Codigo=models.IntegerField(primary_key=True)
            Nombre=models.CharField(max_length=25)
            Precio=models.FloatField()
            Descripcion=models.CharField(max_length=100)
            Imagen=models.ImageField(upload_to="Productos",null=True)

            def __int__(self):
                self.Codigo

