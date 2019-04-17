from addmaterial.models import ProductType
from django import template
from django.db.models import Sum
# Create your views here.

register = template.Library()

@register.filter
def unitsum(id):
    producttype = ProductType.objects.get(pk=id)
    summ = producttype.addmaterial.aggregate(Sum('unit'))['unit__sum']
    return summ
