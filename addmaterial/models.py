from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProductType(models.Model):
    type = models.CharField(max_length=100,  null=True, blank=True)

    def __str__(self):
        return self.type


class AddMaterial(models.Model):
    product_typeadd = models.ForeignKey(ProductType,related_name='addmaterial', on_delete=models.CASCADE,  null=True, blank=True)
    user = models.ForeignKey(User, related_name='addmaterial', on_delete=models.CASCADE, null=True, blank=True)
    input_quality = models.CharField(max_length=100)
    unit = models.IntegerField(max_length=100)
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product_typeadd.type + ' - ' + ' - ' + self.user.username + ' - ' + self.comment + ' - ' + self.unit.__str__()
