from pages.regester_while_checkout import RegisterWhileCheckout
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestRegisterWhileCheckout:
    def test_register_checkout(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        obj=RegisterWhileCheckout(self.driver)
        
        #add product
        obj.add_product()
        
        #view cart
        obj.view_cart()
        
        #click proceed to checkout
        obj.proceed_to_checkout()
        
        #click register/login
        obj.click_register_login()
        
        # signup and create account
        obj.signup()
        
        #Verify 'ACCOUNT CREATED!
        res1=obj.account_created_visible()
        assert res1 == "ACCOUNT CREATED!"
        print("✅ Verify 'ACCOUNT CREATED!")
        
        #click 'Continue' button
        obj.continue_after_create()
        
        #Verify ' Logged in as username' at top
        res2=obj.logged_in_as_visible()
        assert res2 == "Logged in as Amit Shukla"
        print("✅ Verify ' Logged in as username' at top")
        
        #Click 'Cart' button
        obj.click_cart()
        
        #Click 'Proceed To Checkout' button
        obj.proceed_to_checkout()
        
        #Verify Address Details
        address=obj.verify_address()
        assert address == "Address Details"
        print("✅ Verify Address Details")
        
        #Verify Review Your Order
        review=obj.verify_review()
        assert review == "Review Your Order"
        print("✅ verify - Review Your Order")
        
        #Enter description in comment text area and click 'Place Order'
        obj.place_order("Proceed to payment")
        
        # Enter payment details: Name on Card, Card Number, CVC, Expiration date 
        obj.payment("Amit",545584827424,423,11,2031)
        
        #Click 'Pay and Confirm Order' button
        obj.click_and_pay()
        
        msg=obj.final_msg()
        assert msg == "Congratulations! Your order has been confirmed!"
        print("✅ Verify - Congratulations! Your order has been confirmed!")
        
        #Click 'Delete Account' button
        obj.delete_account()
        sleep(2)
        
        #Verify that 'ACCOUNT DELETED!' is visible
        verify=obj.account_deleted_visible()
        assert verify == "ACCOUNT DELETED!"
        print("✅ Verify that 'ACCOUNT DELETED!' is visible")
        
        #click 'Continue' button
        obj.continue_after_delete()
        
        
        