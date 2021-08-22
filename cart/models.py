from django.db import models
from app.models import *

class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)


    class Meta:

        verbose_name='cartlist'
        verbose_name_plural='cartlist'


    def __str__(self):
        return self.cart_id

class items(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.product

    def total(self):
        return self.product.price*self.quantity