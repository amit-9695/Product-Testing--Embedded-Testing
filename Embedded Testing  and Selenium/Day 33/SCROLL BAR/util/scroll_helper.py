class ScrollHelper:
    
    def __init__(self, driver):
        self.driver = driver
     
    # Perfoms scroll by a specific amount of pixels   
    # here x is horizontal scroll and y is vertical scroll
    # so here we set x =0 that we want to scroll vertically only
    def scroll_by_pixel(self, x=0, y=0):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
    
        
    # Scrolls to the bottom of the page
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    
    # Scrolls to the top of the page
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)") 
        
        
    # Scrolls to a specific element on the page
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)