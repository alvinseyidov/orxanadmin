from django.db import models
from addmaterial.models import ProductType
from django.contrib.auth.models import User
# Create your models here.




class OutMaterial(models.Model):
    product_typeout = models.ForeignKey(ProductType,related_name='outmaterial',  on_delete=models.CASCADE,  null=True, blank=True)
    output_quality = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, related_name='outmaterial', on_delete=models.CASCADE, null=True, blank=True)
    unit = models.IntegerField(max_length=100, null=True, blank=True)
    received = models.IntegerField(max_length=100, null=True, blank=True)
    used_type = models.CharField(max_length=100, null=True, blank=True)
    id_number = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product_typeout.type + ' - ' +  self.user.username + ' - ' + self.comment + ' - ' + self.unit.__str__()
