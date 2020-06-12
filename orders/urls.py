from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("menu/<str:category>", views.menu_view, name="menu"),
	path("add_item", views.add_item, name="add_item"),
	path("cart", views.cart_view, name="cart"),
	path("remove_item", views.remove_item, name="remove_item"),
	path("place_order", views.place_order, name="place_order"),
	path("orders", views.orders_view, name="orders"),
	path("complete_order", views.complete_order, name="complete_order")
]