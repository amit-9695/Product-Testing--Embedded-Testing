# Test Case 12: Add Products in Cart
from pages.add_product_cart import AddProductPage
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestAddProduct:
    def test_add_product(self):
        #finding the title of home page after launching the website
        title=self.driver.title
        assert title == "Automation Exercise"
        print("✅ Verify - home page is visible successfully")
        sleep(2)
        
        obj=AddProductPage(self.driver)
        obj.add_cart()
        sleep(4)
        
        obj.view_cart()
        
        name=obj.product_name()
        print("Products Name :- ",name)
        price=obj.product_PRICE()
        print("Products Price :- ",price)
        quantity=obj.product_quantity()
        print("Products Quantity :- ",quantity)
        total=obj.product_total_price()
        print("Products Total Price :- ",total)
        
        print("✅Verify their prices, quantity and total price")