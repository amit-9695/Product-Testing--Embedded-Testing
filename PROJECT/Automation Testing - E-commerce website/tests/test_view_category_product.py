from pages.view_cateogry_products import ViewCategoryProduct
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestViewCategoryProduct:
    def test_view_category_product(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        obj=ViewCategoryProduct(self.driver)
        obj.scroll_by_operation(0,350)
        
        #Verify that categories are visible on left side bar
        category=obj.is_category_visible()
        assert category == "CATEGORY"
        print("✅ Verify that categories are visible on left side bar")
        
        #Click on 'Women' category
        obj.click_women_category()
        
        #Click on any category link under 'Women' category, for example: Dress
        obj.click_dress_sub_category()
        
        #Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
        category_msg_woment=obj.is_women_catgeory_dress_visible()
        assert category_msg_woment == "WOMEN - DRESS PRODUCTS"
        print("✅ Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'")
        
        #On left side bar, click on any sub-category link of 'Men' category
        obj.click_men_category()
        obj.click_sub_category_men()
        
        #Verify that user is navigated to that category page
        category_msg_ment=obj.is_men_catgeory_dress_visible()
        assert category_msg_ment == "MEN - TSHIRTS PRODUCTS"
        print("✅ Verify that user is navigated to that category page")
        
        
        