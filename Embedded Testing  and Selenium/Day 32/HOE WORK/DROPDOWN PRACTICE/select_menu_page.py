from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class SelectMenuPage:
    def __init__(self,driver):
        self.driver=driver
        self.dropdown= (By.XPATH, "//select[@name='country']")
        
    def select_text(self, text):
        dropdown_element=self.driver.find_element(*self.dropdown)
        select =Select(dropdown_element)
        select.select_by_visible_text(text)
        
    def get_selected_option(self):
        dropdown_element = self.driver.find_element(*self.dropdown)
        select = Select(dropdown_element)
        return select.first_selected_option.text