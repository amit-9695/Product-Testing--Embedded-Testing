# Test Case 11: Verify Subscription in Cart page
from pages.subscription_cart_page import SubscribeCartPage
from time import sleep
import pytest
from configs.config import Config

@pytest.mark.usefixtures('init_driver')
class TestSubscriptionCart:
    def test_subscription_cart(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        obj = SubscribeCartPage(self.driver)
        
        #Click 'Cart' button and scroll down to footer
        obj.cart_page()
        obj.scroll_bottom()
        
        # Verify text 'SUBSCRIPTION'
        actual=obj.verify_subscribe_page()
        expected="SUBSCRIPTION"
        assert actual == expected
        print("✅ Verify text 'SUBSCRIPTION'")
        
        #. Enter email address in input and click arrow button
        obj.subscribe_page(Config.EMAIL)
        
        # Verify success message 'You have been successfully subscribed!' is visible
        success=obj.sucess_message_page()
        assert success == "You have been successfully subscribed!"
        print("✅ Verify success message 'You have been successfully subscribed!' is visible")