from django.db import models

from products.models import *
from accounts.models import *


class Cart(models.Model):
    item 				= models.ForeignKey(Items, on_delete=models.CASCADE , default=None )
    quantity 			= models.IntegerField(default=1)
    timestamp 			= models.DateTimeField(auto_now_add=True)
    #user 				= models.ForeignKey(User, on_delete=models.CASCADE , default=None ) 


     
    def __str__(self):
        return f'{self.item}'
    


class Order(models.Model):
    orderitems  		= models.ManyToManyField(Cart)
    user 				= models.ForeignKey(User, on_delete=models.CASCADE)
    ordered 			= models.BooleanField(default=False)
    timestamp 			= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if ordered == False:
        	return f'available'
        else:
        	return f'sold'