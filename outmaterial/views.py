from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OutMaterial
from .forms import OutMaterialForm




@login_required(login_url='/login/')
def outmaterial(request):
    outmaterials = OutMaterial.objects.all()



    if request.method == 'POST':
        form = OutMaterialForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.input_quality = request.POST.get("input_quality")
            model_instance.unit = request.POST.get("unit")
            model_instance.date = request.POST.get("date")
            model_instance.comment = request.POST.get("comment")
            model_instance.save()
            outmaterials = OutMaterial.objects.all()

            return render(request, 'outmaterial.html', {'outmaterials': outmaterials})



    else:

        form = OutMaterialForm()


    return render(request, "outmaterial.html", {'outmaterials': outmaterials,'form': form})
