def update_cart(cart, item, qty):
    cart[item] = qty
    return cart

cart = {
    "T-Shirt": 2,
    "Shoes": 1
}
cart = update_cart(cart, "T-Shirt", 3)
print(cart)

cart = update_cart(cart, "Watch", 1)
print(cart)