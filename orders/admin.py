from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Topping, Sub, Extra, Pasta, Salad, DinnerPlatter, Category, Cart, Order

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)