# Test Case 9: Search Product
from pages.search_product import SearchProduct
from pages.view_product_detail import ViewProductPage
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestSearchProdect:
    def test_search_produt(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        #Click on 'Products' button
        view_product_obj=ViewProductPage(self.driver)
        view_product_obj.click_product()
        
        #Verify user is navigated to ALL PRODUCTS page successfully
        search_product_obj=SearchProduct(self.driver)
        txt=search_product_obj.all_product()
        assert txt == "ALL PRODUCTS"
        print("Verify user is navigated to ALL PRODUCTS page successfully")
        
        #Enter product name in search input and click search button
        #. Verify 'SEARCHED PRODUCTS' is visible
        searched_product = "Men Tshirt"
        search_product_obj.search_product(searched_product)
        expected_product=search_product_obj.item_name()
        assert searched_product == expected_product
        print("Verify 'SEARCHED PRODUCTS' is visible")
        
        