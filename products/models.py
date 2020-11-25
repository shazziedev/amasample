from django.db import models

from accounts.models import User


class Category(models.Model):
	name		= models.CharField(max_length=600)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Items(models.Model):
	name 		= models.CharField(max_length=600)
	price		= models.IntegerField(default=0.00)
	discount	= models.IntegerField(default=0.00)
	location	= models.CharField(max_length=200)
	details		= models.TextField(default=None, null=True, blank=True, help_text='details about the item(s)')
	is_sold		= models.BooleanField(default=False)
	category	= models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
	seller		= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	timestamp	= models.DateTimeField(auto_now_add=True)
	#photo		= models.ImageField(upload_to='items/')

	def __str__(self):
		return f'{self.name} by {self.seller}'

	def get_actual_price(self):
		return self.price

	def get_discount(self):
		return self.discount

	def get_price(self):
		if self.discount > 0.01 and self.discount < self.price:
			return self.price - self.discount
		else:
			return self.price
	
	