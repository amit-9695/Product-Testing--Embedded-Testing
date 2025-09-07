#  Test Case 13: Verify Product quantity in Cart

from pages.product_quantity import ProductQuantityPage
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestProductQty:
    def test_product_qty(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        
        obj=ProductQuantityPage(self.driver)
        
        #Click 'View Product' for any product on home page
        obj.view_product()
        
        product_detail_page=self.driver.current_url
        assert product_detail_page == "https://automationexercise.com/product_details/1"
        print("✅ Verify product detail is opened")
        
        #Increase quantity to 4
        obj.increase_qty("4")
        
        #Click 'Add to cart' button
        obj.add_cart()
        
        #Click 'View Cart' button
        obj.view_cart()
        
        cart_qty=obj.product_qty_cart()
        assert cart_qty == "14"
        print("✅Verify that product is displayed in cart page with exact quantity")
        
        
        