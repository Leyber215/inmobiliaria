from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import PropertyForm
from .models import Property, PropertyBuy
from django.contrib.auth.decorators import login_required


# Create your views here.


def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        properties = Property.objects.all()
        context = {
            "properties": properties,
            "form": form
        }
        return render(request,"properties/property_list.html", context=context)
    else:
        form = PropertyForm()
        context = {
            "form": form
        }
        return render(request, "properties/property_form.html",context=context)
    
def property_detail(request, property_id):
    print(request.method)
    property = get_object_or_404(Property, pk=property_id)  # Asegúrate de importar el modelo adecuado
    return render(request, 'property_detail.html', {'property': property})
    # return render(request, 'property_detail.html', context=context)

@login_required
def buy_property(request, property_id):
    usuario = request.user
    # Obtener la propiedad seleccionada
    propiedad = Property.objects.get(pk=property_id)
    # Crear una nueva instancia de PropertyBuy
    property_buy = PropertyBuy(buyer=usuario, property=propiedad)
    # Guardar en la base de datos
    property_buy.save()
    return HttpResponse("Compra realizada con éxito")
