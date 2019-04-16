from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AddMaterial
from .forms import AddMaterialForm
# Create your views here.


@login_required(login_url='/login/')
def addmaterial(request):
    addmaterials = AddMaterial.objects.all()



    if request.method == 'POST':
        form = AddMaterialForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.input_quality = request.POST.get("input_quality")
            model_instance.unit = request.POST.get("unit")
            model_instance.date = 'request.POST.get("date")'
            model_instance.comment = request.POST.get("comment")
            model_instance.save()
            addmaterials = AddMaterial.objects.all()

            return render(request, 'addmaterial.html', {'addmaterials': addmaterials})



    else:

        form = AddMaterialForm()


    return render(request, "addmaterial.html", {'addmaterials': addmaterials,'form': form})
