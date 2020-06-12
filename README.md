# Pizza Frenzy
Pizza restaurant's ordering web application
![Pizza Frenzy](https://i.imgur.com/QI0gADY.png)

## Link
https://pizzafrenzy.herokuapp.com

## Demo
https://youtu.be/_ukRmoexWnA

## Functions
### 1. Register
Register with a username, password, first name, last name and email address. Checks if email address is already in use, username already exists or entered passwords do not match.
![Registration Page](https://i.imgur.com/Wio2DRe.png)
* `register.html`

### 2. Login
Login to web application with registered username and password. Checks if username/password is invalid.
![Login Page](https://i.imgur.com/gyGcw0W.png)
* `login.html`

### 3. Item Selection
Supports all the available menu items for [Pinocchio's Pizza & Subs](http://www.pinocchiospizza.net/menu.html "Pinocchio's Pizza & Subs Menu"). A customer can toggle the different food categories via the menu side-bar and add items to his/her cart after selecting the desired size, toppings (dropdown) and/or extras (checkbox), if any. 3 toppings are randomly generated for the special regular and sicilian pizzas.
![Menu Page](https://i.imgur.com/KBk0lOZ.png)
* `menu.html`

### 4. Shopping Cart
Displays the details of all outstanding items before an order is placed. Items in cart are saved even if a customer closes the window or logs out and logs back in. A customer can only checkout his/her items after checking the 'confirm order' checkbox.
![Cart Page](https://i.imgur.com/6gqKQob.png)
* `cart.html`

### 5. Order Status
Displays the status (pending/completed) of placed orders for each individual customer. For site administrators, all placed orders will be displayed and they can change the status of pending orders to completed, which will be reflected in a customer's order view. **(personal touch)**
![Orders Page](https://i.imgur.com/UX2b8rp.png)
* `orders.html`