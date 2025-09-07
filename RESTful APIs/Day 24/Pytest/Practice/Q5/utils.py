def calculate_cart_total(cart):
    total = 0
    for item in cart:
        price = item["price"]
        qty = item["qty"]
        discount = item.get("discount", 0)
        total += (price * qty) * (1 - discount)
    return round(total, 2)
