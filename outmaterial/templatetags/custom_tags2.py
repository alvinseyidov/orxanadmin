from addmaterial.models import ProductType
from django import template
from django.db.models import Sum
# Create your views here.

register = template.Library()

@register.filter
def unitsum2(id):
    producttypeout = ProductType.objects.get(pk=id)
    summ2 = producttypeout.outmaterial.aggregate(Sum('unit'))['unit__sum']
    return summ2
