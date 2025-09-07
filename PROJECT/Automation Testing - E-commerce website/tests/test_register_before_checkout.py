#Test Case 15: Place Order: Register before Checkout
from pages.register_before_checkout import RegisterBeforeCheckout
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestRegisterBeforeCheckout:
    def test_register_before_checkout(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        obj=RegisterBeforeCheckout(self.driver)
        
        #Click 'Signup / Login' button
        obj.click_signup_btn()
        
        #Fill all details in Signup and create account
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
        
        #Add products to cart
        obj.scroll_by_operation(0,450)
        obj.add_product()
        
        #view cart
        obj.view_cart()
        #Verify that cart page is displayed
        cart_page_url=self.driver.current_url
        assert cart_page_url== "https://automationexercise.com/view_cart"
        print("✅ Verify that cart page is displayed")
        
        #click proceed to checkout
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