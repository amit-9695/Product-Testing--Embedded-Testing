# Test Case 17: Remove Products From Cart
from pages.remove_product import RemoveProduct
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestRemoveProduct:
    def test_remove_product(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        obj=RemoveProduct(self.driver)
        
        #Add products to cart
        obj.add_product()
        
        # Click 'Cart' button
        obj.open_cart()
        
        #Verify that cart page is displayed
        cart_page_url=self.driver.current_url
        assert cart_page_url == "https://automationexercise.com/view_cart"
        print("✅ Verify that cart page is displayed")
        
        #Click 'X' button corresponding to particular product
        obj.remove_product()
        
        #Verify that product is removed from the cart 
        empty=obj.veify_empty()
        assert empty == "Cart is empty! Click here to buy products."
        print("✅ Verify that product is removed from the cart")