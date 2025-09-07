from utils import calculate_cart_total

def test_cart_total_basic():
    cart = [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]
    assert calculate_cart_total(cart) == 250.0

def test_cart_with_discounts():
    cart = [
        {"price": 100, "qty": 2, "discount": 0.1},  # 10% off
        {"price": 50, "qty": 1}
    ]
    assert calculate_cart_total(cart) == 230.0
