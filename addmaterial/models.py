from django.db import models

# Create your models here.

class AddMaterial(models.Model):
    MERKEZ = 'MRK'
    FILIAL = 'FLL'

    CLINIC_TYPES = (
        (MERKEZ, 'Merkez'),
        (FILIAL, 'filial')
    )

    product_type = models.CharField(max_length=25, choices=CLINIC_TYPES, null=True, blank=True)
    input_quality = models.CharField(max_length=100)
    unit = models.IntegerField(max_length=100)
    date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product_type
