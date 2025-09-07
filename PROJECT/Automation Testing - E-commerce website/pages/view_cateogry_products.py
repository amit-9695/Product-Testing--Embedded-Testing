from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewCategoryProduct(BasePage):
    CATEGORY=(By.XPATH,'/html/body/section[2]/div/div/div[1]/div/h2')
    WOMEN=(By.XPATH,'//*[@id="accordian"]/div[1]/div[1]/h4/a/span/i')
    DRESS=(By.XPATH,'//*[@id="Women"]/div/ul/li[1]/a')
    CONFIRM_MSG_WOMEN=(By.XPATH,'/html/body/section/div/div[2]/div[2]/div/h2')
    MEN=(By.XPATH,'//*[@id="accordian"]/div[2]/div[1]/h4/a/span/i')
    T_SHIRT=(By.XPATH,'//*[@id="Men"]/div/ul/li[1]/a')
    CONFIRM_MSG_MEN=(By.XPATH,'/html/body/section/div/div[2]/div[2]/div/h2')
    
    def is_category_visible(self):
        return self.find_web_element(self.CATEGORY).text
    
    def click_women_category(self):
        self.click_operation(self.WOMEN)
        
    def click_dress_sub_category(self):
        self.click_operation(self.DRESS)
        
    def is_women_catgeory_dress_visible(self):
        return self.find_web_element(self.CONFIRM_MSG_WOMEN).text
    
    def click_men_category(self):
        self.click_operation(self.MEN)
        
    def click_sub_category_men(self):
        self.click_operation(self.T_SHIRT)
        
    def is_men_catgeory_dress_visible(self):
        return self.find_web_element(self.CONFIRM_MSG_MEN).text