from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)
  

@login_required(login_url = "/admin/login/")
@permission_required('vehiculos.add_vehiculo', login_url = "/admin/login/")
def v_add(request):
    if request.method == 'POST':
      data = VehiculoForm(request.POST)
      if data.is_valid(): #los datos pasan las validaciones
        data.save()
        
    context = {"form": VehiculoForm()}
    return render(request, "add.html", context)
  

@login_required(login_url = "/admin/login/")
@permission_required('vehiculos.visualizar_catalogo', login_url = "/admin/login/")
def v_list(request):
  context={
    'cars': Vehiculo.objects.all()}
  return render(request,'listar.html', context)

## user reportes pass: %passw0rd%
## user agrega pass: %passw0rd%