from django.db import models

# Create your models here.


class ProductType(models.Model):
    type = models.CharField(max_length=100,  null=True, blank=True)

    def __str__(self):
        return self.type


class AddMaterial(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE,  null=True, blank=True)
    input_quality = models.CharField(max_length=100)
    unit = models.IntegerField(max_length=100)
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.comment
