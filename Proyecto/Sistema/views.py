from django.shortcuts import render,get_object_or_404,redirect
from .models import Productos
from .formularios import NewProducts

# Create your views here.
def Home(request):
    data={
        'Home':Home
    }
    return render(request,"index.html",data)

def Registrar(request):
    data = {
        'form':NewProducts()
    }
    if request.method=='POST':
        guardar=NewProducts(data=request.POST,files=request.FILES)
        if guardar.is_valid():
            guardar.save()
            data["mensaje"]="datos guardados"
        else:
            data["form"]=guardar
            
    return render(request,"Pages/registrar.html",data)
def Listar(request):
    Listar=Productos.objects.all()
    data={
        'Listar':Listar
    }
    return render(request,"Pages/listar.html",data)

def eliminar(request,Codigo):
    buscar=get_object_or_404(Productos,Codigo=Codigo)
    buscar.delete()
    return redirect(to=Listar) 
def modificar(request,Codigo):
    sql=get_object_or_404(Productos,Codigo=Codigo)
    data={
        'forms':NewProducts(instance=sql)
    }
    if request.method=='POST':
        query=NewProducts(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Modificados Correctamente "
        else:
            data['forms']=NewProducts
    return render (request,'Pages/modificar.html',data)
