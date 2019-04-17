from addmaterial.models import ProductType
from django import template
from django.db.models import Sum
# Create your views here.

register = template.Library()

@register.filter
def unitsum3(id):
    producttypeadd = ProductType.objects.get(pk=id)
    sum0 = 0
    summ2 = 0
    if producttypeadd.addmaterial.all().count() > 0:
        summ = producttypeadd.addmaterial.aggregate(Sum('unit'))['unit__sum']
    if producttypeadd.outmaterial.all().count() > 0:
        summ2 = producttypeadd.outmaterial.aggregate(Sum('unit'))['unit__sum']

    return summ - summ2
