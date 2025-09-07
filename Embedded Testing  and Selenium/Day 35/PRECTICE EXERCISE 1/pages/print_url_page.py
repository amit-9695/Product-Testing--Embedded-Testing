from pages.navigate_url import Navigate
from config.config import Config

class PrintUrl(Navigate):
    def print_url(self):
        self.navigate_url()
        