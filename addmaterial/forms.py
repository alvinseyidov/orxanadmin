from django import forms
from .models import AddMaterial

class AddMaterialForm(forms.ModelForm):

    class Meta:
        model = AddMaterial
        fields = ['product_type']
