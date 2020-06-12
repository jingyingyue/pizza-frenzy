document.addEventListener('DOMContentLoaded', () => {

	// when user adds item to cart
	document.querySelectorAll('.plus').forEach((plus) => {
		// add click event to each add item plus sign
		plus.addEventListener('click', (e) => {
			// show menu-form
			$('#menu-form').modal('show');

			// update hidden input values
			document.querySelector('#input-name').value = e.target.dataset.name;
			document.querySelector('#input-size').value = e.target.dataset.size;
			document.querySelector('#input-price').value = e.target.dataset.price;
			document.querySelector('#input-category').value = e.target.dataset.category;

			// show selected item name, size (if any) and price
			document.querySelector('#name').innerHTML = e.target.dataset.category+' - '+e.target.dataset.name;
			if (e.target.dataset.size) {
				document.querySelector('#size').innerHTML = e.target.dataset.size;
			};
			document.querySelector('#price').innerHTML = '$'+e.target.dataset.price;
			document.querySelector('#price').dataset.price = e.target.dataset.price;

			// toggle pizza topping select visibility
			if (e.target.dataset.category==='Regular Pizza' && e.target.dataset.name==='Cheese') {
				document.querySelector('#toppings').style.display = 'none';
			}
			if (e.target.dataset.category==='Sicilian Pizza' && e.target.dataset.name==='Cheese') {
				document.querySelector('#toppings').style.display = 'none';
			}
			else if (e.target.dataset.name==='1 topping' || e.target.dataset.name==='1 item') {
				document.querySelector('#toppings').style.display = 'inline';
				document.querySelector('#topping1').style.display = 'inline';
				document.querySelector('#topping2').style.display = 'none';
				document.querySelector('#topping3').style.display = 'none';
			}
			else if (e.target.dataset.name==='2 toppings' || e.target.dataset.name==='2 items') {
				document.querySelector('#toppings').style.display = 'inline';
				document.querySelector('#topping1').style.display = 'inline';
				document.querySelector('#topping2').style.display = 'inline';
				document.querySelector('#topping3').style.display = 'none';
			}
			else if (e.target.dataset.name==='3 toppings' || e.target.dataset.name==='3 items' || e.target.dataset.name==='Special') {
				document.querySelector('#toppings').style.display = 'inline';
				document.querySelector('#topping1').style.display = 'inline';
				document.querySelector('#topping2').style.display = 'inline';
				document.querySelector('#topping3').style.display = 'inline';
			};

			// random select toppings for special pizza
			if (e.target.dataset.name==='Special') {
				randomSelect('#topping1');
				randomSelect('#topping2');
				randomSelect('#topping3');
			}
			else if (e.target.dataset.name==='3 toppings' || e.target.dataset.name==='3 items') {
				document.querySelector('#topping1').selectedIndex = 0;
				document.querySelector('#topping2').selectedIndex = 0;
				document.querySelector('#topping3').selectedIndex = 0;
			};

			// toggle sub extra checkbox visibility
			if (e.target.dataset.name==='Steak + Cheese') {
				document.querySelector('#check-extra1').style.display = 'block';
				document.querySelector('#check-extra2').style.display = 'block';
				document.querySelector('#check-extra3').style.display = 'block';
				document.querySelector('#check-extra4').style.display = 'block';
			}
			else if (e.target.dataset.category==='Sub') {
				document.querySelector('#check-extra1').style.display = 'none';
				document.querySelector('#check-extra2').style.display = 'none';
				document.querySelector('#check-extra3').style.display = 'none';
				document.querySelector('#check-extra4').style.display = 'block';
			};

			// reset menu-form if user exits without adding item to cart
			$('#menu-form').on('hidden.bs.modal', function() {
			    $(this).find('form')[0].reset();
			});
		});
	});


	// when user adds/removes extra to/from sub
	document.querySelectorAll('.form-check-input').forEach((box) => {
		// add click event to each add extra checkbox
		box.addEventListener('click', (e) => {
			const extra_price = document.getElementById(e.target.dataset.priceid);
			const curr_price = document.querySelector('#price');

			// if adding extra, add extra price to current price
			if (extra_price.value=='0.00') {
				extra_price.value = e.target.dataset.price;
				var new_price = parseFloat(curr_price.dataset.price)+parseFloat(e.target.dataset.price);
			}
			// if removing extra, subtract extra price from current price
			else {
				extra_price.value = '0.00';
				var new_price = parseFloat(curr_price.dataset.price)-parseFloat(e.target.dataset.price);
			};

			// update current price
			curr_price.innerHTML = '$'+new_price.toFixed(2);
			curr_price.dataset.price = new_price.toFixed(2);

			// reset menu-form if user exits without adding item to cart
			$('#menu-form').on('hidden.bs.modal', function() {
			    $(this).find('form-check').trigger('reset');
			    curr_price.innerHTML = '$'+document.querySelector('#input-price').value;
			    curr_price.dataset.price = document.querySelector('#input-price').value;
			    extra_price.value = '0.00'
			});
		});
	});


	// enable checkout-button if confirm-order-box is checked
	document.querySelectorAll('#confirm-order-box').forEach((box) => {
		box.onclick = function() {
			if (this.checked) {
				document.querySelector('#checkout-button').disabled = false;
			}
			else {
				document.querySelector('#checkout-button').disabled = true;
			};
		};
	});

});


function randomSelect(select_id) {
	// select a random option //
	var select = document.querySelector(select_id);
	var items = select.getElementsByTagName('option');
	var index = Math.floor(Math.random()*items.length);
	select.selectedIndex = index;
}