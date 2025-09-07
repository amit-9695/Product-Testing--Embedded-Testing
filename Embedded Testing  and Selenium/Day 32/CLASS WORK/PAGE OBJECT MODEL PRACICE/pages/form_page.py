from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver

class FormPage:
    # TAKING URL FOR THE FORM PAGE
    URL= "https://www.w3schools.com/html/html_forms.asp"
    
    # TAKING LOCATORS FOR THE FORM FIELDS
    FIRST_NAME = (By.NAME, "fname")
    LAST_NAME = (By.NAME, "lname")
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)
        
    def  load_form(self):
        # Load the form page
        self.driver.get(self.URL)
        self.driver.maximize_window()
        
    def enter_first_name(self, first_name):
        # Find the first name field and enter the value
        first_name_field = self.driver.find_element(*self.FIRST_NAME)
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        
    def enter_last_name(self, last_name):
        # Find the last name field and enter the value
        last_name_field = self.driver.find_element(*self.LAST_NAME)
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        
    def submit_form(self):
        # Submit the form by clicking the submit button
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        self.actions.move_to_element(submit_button).click().perform()
        
    def close_browser(self):
        # Close the browser
        self.driver.quit()
        
        