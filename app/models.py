from django.db import models


CATEGORY_CHOICES=(('AP','APRICOT'),('MB','MALLBERRY'),('WN','WALLNUT'),('PT','PISTACHU'),('AL','ALMOND'),('D','Dates'),)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    


