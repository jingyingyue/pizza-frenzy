from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegularPizza(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.DecimalField(max_digits=4, decimal_places=2)
	price_large = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Small: ${self.price_small}, Large: ${self.price_large}"


class SicilianPizza(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.DecimalField(max_digits=4, decimal_places=2)
	price_large = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Small: ${self.price_small}, Large: ${self.price_large}"


class Topping(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"


class Sub(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	price_large = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Small: ${self.price_small}, Large: ${self.price_large}"


class Extra(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Price: ${self.price}"


class Pasta(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Price: ${self.price}"


class Salad(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Price: ${self.price}"


class DinnerPlatter(models.Model):
	name = models.CharField(max_length=64)
	price_small = models.DecimalField(max_digits=4, decimal_places=2)
	price_large = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} - Small: ${self.price_small}, Large: ${self.price_large}"


class Category(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order_id = models.IntegerField()
	item = models.CharField(max_length=64)
	add_ons = models.CharField(max_length=64)
	size = models.CharField(max_length=10)
	price = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.id} - User: {self.user}, Order ID: {self.order_id}, Item: {self.item}, Add-ons: {self.add_ons}, Size: {self.size}, Price: ${self.price}"


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, default='Initiated')

	def __str__(self):
		return f"{self.id} - User: {self.user}, Total: ${self.total}, Date: {self.date}, Status: {self.status}"