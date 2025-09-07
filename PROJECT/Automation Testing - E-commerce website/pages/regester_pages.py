from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
class RgesterPage(BasePage):
    SIGNUP_LOGIN_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    NEW_USER_SIGNUP=(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/h2')
    NAME_INPUT = (By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    EMAIL_INPUT = (By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    SIGNUP_BTN = (By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button')
    ENTER_ACCOUNT_INFO = (By.XPATH,'//*[@id="form"]/div/div/div/div[1]/h2/b')
    TITLE_MR =(By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/div[1]/div[1]/label')
    PASSWORD_INPUT =(By.XPATH,'//*[@id="password"]')
    DOB_DAY = (By.XPATH,'//*[@id="days"]')
    DOB_MONTH = (By.XPATH,'//*[@id="months"]')
    DOB_YEAR = (By.XPATH,'//*[@id="years"]')
    NEWSLETTER_CHK =(By.XPATH,'//*[@id="newsletter"]')
    SPECIAL_OFFER_CHK = (By.XPATH,'//*[@id="optin"]')
    FIRST_NAME = (By.XPATH,'//*[@id="first_name"]')
    LAST_NAME = (By.XPATH,'//*[@id="last_name"]')
    COMPANY = (By.XPATH,'//*[@id="company"]')
    ADDRESS1 = (By.XPATH,'//*[@id="address1"]')
    ADDRESS2 = (By.XPATH,'//*[@id="address2"]')
    COUNTRY = (By.XPATH,'//*[@id="country"]')
    STATE = (By.XPATH,'//*[@id="state"]')
    CITY = (By.XPATH,'//*[@id="city"]')
    ZIPCODE = (By.XPATH,'//*[@id="zipcode"]')
    MOBILE = (By.XPATH,'//*[@id="mobile_number"]')
    CREATE_ACCOUT_BTN = (By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/button')
    ACCOUNT_CREATED = (By.XPATH,'//*[@id="form"]/div/div/div/h2/b')
    CONTINUE_BTN = (By.XPATH,'//*[@id="form"]/div/div/div/div/a')
    LOGGED_IN_AS = (By.XPATH,'//a[contains(text(),"Logged in as")]')
    DELETE_ACCOUNT_BTN =(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    ACCOUNT_DELETED= (By.XPATH,'//*[@id="form"]/div/div/div/h2/b')
    CONTINUE_AFTER_DELETE = (By.XPATH,'//*[@id="form"]/div/div/div/div/a')
    
    # Click on Signup/Login button
    def goto_singup_login(self):
        self.click_operation(self.SIGNUP_LOGIN_BTN)
    
    # Enter the Data to the Sign up section and click signup
    def enter_signup_details(self,name,email):
        self.enter_value_operation(self.NAME_INPUT,name)
        self.enter_value_operation(self.EMAIL_INPUT,email)
        self.click_operation(self.SIGNUP_BTN)
        
    # Filling Account Info after clicking the signup button
    def fill_account_info(self,password,day,mon,year):
        self.scroll_by_operation(0,200)
        self.click_operation(self.TITLE_MR)
        self.enter_value_operation(self.PASSWORD_INPUT,password)
        self.enter_value_operation(self.DOB_DAY,day)
        self.enter_value_operation(self.DOB_MONTH,mon)
        self.enter_value_operation(self.DOB_YEAR,year)
        
        self.scroll_by_operation(0,400)
        self.click_operation(self.NEWSLETTER_CHK)
        self.click_operation(self.SPECIAL_OFFER_CHK)
    
        
    def address_info(self,first_name,last_name,company,address1,address2,country,state,city,zipcode,mobile_number):
        self.scroll_by_operation(0,200)
        self.enter_value_operation(self.FIRST_NAME,first_name)
        self.enter_value_operation(self.LAST_NAME,last_name)
        self.enter_value_operation(self.COMPANY,company)
        self.enter_value_operation(self.ADDRESS1,address1)
        self.enter_value_operation(self.ADDRESS2,address2)
        self.enter_value_operation(self.COUNTRY,country)
        
        self.scroll_by_operation(0,350)
        self.enter_value_operation(self.STATE,state)
        self.enter_value_operation(self.CITY,city)
        self.enter_value_operation(self.ZIPCODE,zipcode)
        self.enter_value_operation(self.MOBILE,mobile_number)
    
    # Create account button 
    def create_account(self):
        self.click_operation(self.CREATE_ACCOUT_BTN)
        
    #Verify that 'ACCOUNT CREATED!' is visible
    def account_created_visible(self):
        return self.find_web_element(self.ACCOUNT_CREATED).text
        
    # Countnue after creating account button
    def continue_after_create(self):
        self.click_operation(self.CONTINUE_BTN)
        
    #Verify that 'Logged in as username' is visible
    def logged_in_as_visible(self):
        return self.find_web_element(self.LOGGED_IN_AS).text
    
    #Click 'Delete Account' button
    def delete_account(self):
        self.click_operation(self.DELETE_ACCOUNT_BTN)
        
    #Verify that 'ACCOUNT DELETED!' is visible
    def account_deleted_visible(self):
        return self.find_web_element(self.ACCOUNT_DELETED).text
    
    #click 'Continue' button
    def continue_after_delete(self):
        self.click_operation(self.CONTINUE_AFTER_DELETE)
        
    
    
        
    
        
       
    
    