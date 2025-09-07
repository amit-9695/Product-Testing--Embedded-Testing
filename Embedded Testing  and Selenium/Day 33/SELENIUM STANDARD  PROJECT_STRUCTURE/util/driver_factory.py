from selenium import webdriver

def get_driver(browser):
    if browser.lower() == 'chrome':
        return webdriver.Chrome()
        
    elif browser.lower() == 'firefox':
        return webdriver.Firefox()
        
    elif browser.lower() == 'edge':
        return webdriver.Edge()
    
    else:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers are Chrome, Firefox, and Edge.")
    
    