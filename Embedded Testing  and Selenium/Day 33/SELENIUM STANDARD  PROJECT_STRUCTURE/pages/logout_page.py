from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class LogoutPage(BasePage):
    """Page object for the logout page of the application."""
    SELECTOR_LOCATOR = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_BUTTON_LOCATOR = (By.ID, "logout_sidebar_link")
    
    def logout(self):
        """Perform logout action."""
        
        actions= ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.SELECTOR_LOCATOR)).perform()
        actions.click(self.driver.find_element(*self.SELECTOR_LOCATOR)).perform()
       
       