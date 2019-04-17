from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from home.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from addmaterial.models import AddMaterial,ProductType
from outmaterial.models import OutMaterial
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    addmaterials = AddMaterial.objects.all()
    producttype = ProductType.objects.all()

    return render(request, "index.html", {'producttypes': producttype})


@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user.html', args)

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user')
        else:
            return redirect('user')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'changepassword.html', args)
