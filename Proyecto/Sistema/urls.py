from django.urls import path
from .views import Listar,Registrar,Home,eliminar,modificar

urlpatterns = [
   path("",Home,name="Home"),
   path("listar/",Listar,name="Listar"),
   path("registrar/",Registrar,name="Registrar"),
   path("eliminar<Codigo>",eliminar,name="eliminar"),
   path("modificar<Codigo>",modificar,name="modificar"),
]
