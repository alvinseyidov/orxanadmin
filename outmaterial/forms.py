from django import forms
from .models import OutMaterial

class OutMaterialForm(forms.ModelForm):

    class Meta:
        model = OutMaterial
        fields = ['product_typeout']
