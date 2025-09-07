# Test Case 10: Verify Subscription in home page
from pages.subscription_page import SubscriptionPage
from time import sleep
import pytest
from configs.config import Config

@pytest.mark.usefixtures("init_driver")
class TestSubscription:
    def test_subscription(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        # Scroll down to footer
        obj=SubscriptionPage(self.driver)
        obj.scroll_botton()
        sleep(2)
        
        #Verify text 'SUBSCRIPTION'
        actul=obj.verify_subscription()
        expected="SUBSCRIPTION"
        assert actul == expected
        print("✅ Verify text 'SUBSCRIPTION'")
        
        #Enter email address in input and click arrow button
        obj.subscribe(Config.EMAIL)
        
        
        
        #Verify success message 'You have been successfully subscribed!' is visible
        ale_txt=obj.get_alert_text()
        assert ale_txt == "You have been successfully subscribed!"
        print("✅ Verify success message 'You have been successfully subscribed!' is visible")
        
        