from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class AddMaterialProductType(models.Model):
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type
