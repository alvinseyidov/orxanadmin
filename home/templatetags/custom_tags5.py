from addmaterial.models import ProductType
from django import template
from django.db.models import Sum
# Create your views here.

register = template.Library()

@register.filter
def unitsum5(id):
    producttypeout = ProductType.objects.get(pk=id)
    summ2 = 0
    if producttypeout.outmaterial.all().count() > 0:
        summ2 = producttypeout.outmaterial.aggregate(Sum('unit'))['unit__sum']
    return summ2
