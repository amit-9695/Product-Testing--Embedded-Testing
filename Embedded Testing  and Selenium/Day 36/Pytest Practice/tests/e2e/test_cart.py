import pytest
from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

@pytest.mark.regression
def test_add_to_cart_and_logout(driver, base_url):
    # Login first
    login = LoginPage(driver)
    login.open(base_url)
    login.login("standard_user", "secret_sauce")
    
    # Inventory actions
    inv = InventoryPage(driver)
    assert inv.is_loaded(), "Inventory should be visible after login"
    inv.add_backpack_to_cart()
    assert inv.cart_count() == 1, "Cart badge should show 1 item"
    
    # Logout
    inv.logout()
    # After logout, login page username field should be visible again
    from selenium.webdriver.common.by import By
    assert login.find((By.ID, "user-name")) is not None