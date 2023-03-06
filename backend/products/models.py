from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)

    @property
    def sale_price(self):
        return f"{float(self.price) * 0.8:.2f}"
    
    def get_discount(self):
        return "122"

    def __str__(self):
        return self.title
