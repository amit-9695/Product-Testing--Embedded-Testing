from selenium.webdriver.common.by import By
from .base_page import BasePage
class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    
    def is_loaded(self) -> bool:
        return self.find(self.INVENTORY_CONTAINER) is not None
    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)
    def cart_count(self) -> int:
        try:
            return int(self.find(self.CART_BADGE).text)
        except Exception:
            return 0
    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_LINK)