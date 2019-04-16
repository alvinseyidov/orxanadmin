from django.db import models

# Create your models here.



class OutMaterial(models.Model):
    MERKEZ = 'MRK'
    FILIAL = 'FLL'

    CLINIC_TYPES = (
        (MERKEZ, 'Merkez'),
        (FILIAL, 'filial')
    )

    product_type = models.CharField(max_length=25, choices=CLINIC_TYPES, null=True, blank=True)
    output_quality = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    received = models.CharField(max_length=100)
    id_material = models.CharField(max_length=100)
    date = models.DateField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type
