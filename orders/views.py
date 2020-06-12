from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import RegularPizza, SicilianPizza, Topping, Sub, Extra, Pasta, Salad, DinnerPlatter, Category, Cart, Order

# Create your views here.
def index(request):
	# check if user is logged in
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	else:
		# fetch items previously in cart, otherwise create new order object and add to database
		try:
			order = Order.objects.get(user=request.user, status='Initiated')
		except:
			order = Order(user=request.user)
			order.save()

		# get cart item count
		cart = Cart.objects.filter(user=request.user, order_id=order.id)
		count = 0
		for item in cart:
			count += 1

		# create context
		context = {
			"user": request.user,
			"categories": Category.objects.all(),
			"count": count
		}

		# redirect user to home page
		return render(request, "orders/index.html", context)


def register_view(request):
	""" register a new user """
	if request.method=="POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		username = request.POST["username"]
		password = request.POST["password"]
		confirm_password = request.POST["confirm_password"]

		# check if email already registered
		if User.objects.filter(email=email).exists():
			return render(request, "orders/register.html", {"message": "Email already registered"})
		
		# check if username already exists
		elif User.objects.filter(username=username).exists():
			return render(request, "orders/register.html", {"message": "Username already exists"})

		# check if two passwords do not match
		elif password!=confirm_password:
			return render(request, "orders/register.html", {"message": "Passwords do not match"})

		else:
			# create new user object and add to database
			user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
			user.save()

			# redirect user to login page
			return render(request, "orders/login.html", {"pass": "Account created"})

	else:
		return render(request, "orders/register.html")


def login_view(request):
	""" login a user """
	if request.method=="POST":
		# check if user entered valid username and password
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# if valid, login user and redirect to home page
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))

		# if invalid, redirect user back to login page
		else:
			return render(request, "orders/login.html", {"fail": "Invalid username/password"})

	else:
		return render(request, "orders/login.html")


def logout_view(request):
	""" logout a user """
	# redirect user to login page
	logout(request)
	return render(request, "orders/login.html", {"pass": "Logged out"})


def menu_view(request, category):
	""" display items in menu """
	# check if user is logged in
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	else:
		# get cart item count
		order = Order.objects.get(user=request.user, status='Initiated')
		cart = Cart.objects.filter(user=request.user, order_id=order.id)
		count = 0
		for item in cart:
			count += 1

		# create context
		context = {
			"user": request.user,
			"categories": Category.objects.all(),
			"selected_category": Category.objects.get(name=category),
			"regular_pizzas": RegularPizza.objects.all(),
			"sicilian_pizzas": SicilianPizza.objects.all(),
			"toppings": Topping.objects.all(),
			"subs": Sub.objects.all(),
			"extras": Extra.objects.all(),
			"pastas": Pasta.objects.all(),
			"salads": Salad.objects.all(),
			"dinner_platters": DinnerPlatter.objects.all(),
			"count": count
		}

	    # redirect user to respective menu page
		return render(request, "orders/menu.html", context)


def add_item(request):
	""" add an item to cart """
	name = request.POST["name"]
	size = request.POST["size"]
	price = float(request.POST["price"])
	category = request.POST["category"]
	add_ons = ''

	# check for pizza toppings added
	if (category=='Regular Pizza') or (category=='Sicilian Pizza'):
		topping1 = request.POST["topping1"]
		topping2 = request.POST["topping2"]
		topping3 = request.POST["topping3"]

		# add toppings to add_ons
		if (name=='1 topping') or (name=='1 item'):
			add_ons += f"{topping1}, "
		if (name=='2 toppings') or (name=='2 items'):
			add_ons += f"{topping1}, {topping2}, "
		if (name=='3 toppings') or (name=='3 items') or (name=='Special'):
			add_ons += f"{topping1}, {topping2}, {topping3}, "

	# check for sub extras added
	if category=='Sub':
		try:
			extra1 = request.POST["extra1"]
		except:
			extra1 = ''
		try:
			extra2 = request.POST["extra2"]
		except:
			extra2 = ''
		try:
			extra3 = request.POST["extra3"]
		except:
			extra3 = ''
		try:
			extra4 = request.POST["extra4"]
		except:
			extra4 = ''

		# add extras to add_ons and price of extras to price
		if extra1:
			add_ons += f"{extra1}, "
			price += float(request.POST["price1"])
		if extra2:
			add_ons += f"{extra2}, "
			price += float(request.POST["price2"])
		if extra3:
			add_ons += f"{extra3}, "
			price += float(request.POST["price3"])
		if extra4:
			add_ons += f"{extra4}, "
			price += float(request.POST["price4"])

	# check for extra ', ' at end of add_ons and remove
	if add_ons and add_ons[len(add_ons)-1]==' ':
		add_ons = add_ons[:-2]

	# check if item has no size
	if size=='undefined':
		size = ''

	# get order this item falls under and update total price
	order = Order.objects.get(user=request.user, status='Initiated')
	order.total = float(order.total)+price
	order.save()

	# create new cart object and add to database
	cart = Cart(user=request.user,
				order_id=order.id,
				item=category+' - '+name,
				add_ons=add_ons,
				size=size,
				price=price)
	cart.save()

	# redirect user to menu page he/she was on
	return HttpResponseRedirect(reverse("menu", args=(category,)))


def cart_view(request):
	""" display items in cart """
	# check if user is logged in
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	else:
		# get cart item count
		order = Order.objects.get(user=request.user, status='Initiated')
		cart = Cart.objects.filter(user=request.user, order_id=order.id)
		count = 0
		for item in cart:
			count += 1

		# create context
		context = {
			"user": request.user,
			"categories": Category.objects.all(),
			"regular_pizzas": RegularPizza.objects.all(),
			"sicilian_pizzas": SicilianPizza.objects.all(),
			"toppings": Topping.objects.all(),
			"subs": Sub.objects.all(),
			"extras": Extra.objects.all(),
			"pastas": Pasta.objects.all(),
			"salads": Salad.objects.all(),
			"dinner_platters": DinnerPlatter.objects.all(),
			"order": order,
			"cart": cart,
			"count": count
		}

		# redirect user to cart page
		return render(request, "orders/cart.html", context)


def remove_item(request):
	""" remove an item from cart """
	cart_id = request.POST["cart_id"]
	price = request.POST["price"]

	# delete item's cart object
	Cart.objects.filter(id=cart_id).delete()

	# subtract item's price from order's total price
	order = Order.objects.get(user=request.user, status='Initiated')
	order.total = float(order.total)-float(price)
	order.save()

	# redirect user to cart page with remaining items
	return HttpResponseRedirect(reverse("cart"))


def place_order(request):
	""" place a confirmed order """
	# get order and change its status to pending
	order_id = request.POST["order_id"]
	order = Order.objects.get(id=order_id)
	order.status = 'Pending'
	order.save()

	# redirect user to orders page
	return HttpResponseRedirect(reverse("orders"))


def orders_view(request):
	""" display orders """
	# check if user is logged in
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	else:
		# fetch items previously in cart, otherwise create new order object and add to database
		try:
			order = Order.objects.get(user=request.user, status='Initiated')
		except:
			order = Order(user=request.user)
			order.save()

		# get cart item count
		cart = Cart.objects.filter(user=request.user, order_id=order.id)
		count = 0
		for item in cart:
			count += 1

		# create context
		context = {
			"user": request.user,
			"categories": Category.objects.all(),
			"regular_pizzas": RegularPizza.objects.all(),
			"sicilian_pizzas": SicilianPizza.objects.all(),
			"toppings": Topping.objects.all(),
			"subs": Sub.objects.all(),
			"extras": Extra.objects.all(),
			"pastas": Pasta.objects.all(),
			"salads": Salad.objects.all(),
			"dinner_platters": DinnerPlatter.objects.all(),
			"count": count
		}

		# check if user is admin
		if request.user.is_staff:
			# add all pending/completed orders and cart items to context
			context["all_orders"] = Order.objects.all().filter(status='Pending') | Order.objects.all().filter(status='Completed')
			context["all_cart"] = Cart.objects.all()
		else:
			# add user's pending/completed orders and cart items to context
			context["user_orders"] = Order.objects.all().filter(user=request.user, status='Pending') | Order.objects.all().filter(user=request.user, status='Completed')
			context["user_cart"] = Cart.objects.all().filter(user=request.user)

		# redirect user to orders page
		return render(request, "orders/orders.html", context)


def complete_order(request):
	""" mark a pending order as completed """
	# get order and change its status to completed
	order_id = request.POST["order_id"]
	order = Order.objects.get(id=order_id)
	order.status = 'Completed'
	order.save()

	# redirect user to orders page
	return HttpResponseRedirect(reverse("orders"))