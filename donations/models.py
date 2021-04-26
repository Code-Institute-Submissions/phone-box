from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(decimal_places=0, max_digits=3, null=True, blank=True)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name