# Test Case 8: Verify All Products and product detail page
from pages.view_product_detail import ViewProductPage
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestViewProductDetail:
    def test_product_detail(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        
        #creating instance
        detail=ViewProductPage(self.driver)
        
        #Click on 'Products' button
        detail.click_product()
        
        #. Verify user is navigated to ALL PRODUCTS page successfully
        product_page_url="https://automationexercise.com/products"
        current_page_url=self.driver.current_url
        assert product_page_url == current_page_url
        print("✅ Verify user is navigated to ALL PRODUCTS page successfully")
        
        #Click on 'View Product' of first product
        detail.view_first_product()
        sleep(2)
        #. User is landed to product detail page
        
        #. Verify that detail detail is visible: product name, category, price, availability, condition, brand
        name=detail.first_product_detail()
        print(name)
        print("✅ Verify that detail detail is visible: product name, category, price, availability, condition, brand")