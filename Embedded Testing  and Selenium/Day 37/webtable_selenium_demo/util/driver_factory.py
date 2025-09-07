from selenium import webdriver

def get_driver(browser_name="chrome"):
    if browser_name.lower()=="chrome":
        driver=webdriver.Chrome()
    elif browser_name.lower()=="edge":
        driver=webdriver.Edge()
    elif browser_name.lower()=="firefox":
        driver=webdriver.Firefox()
    else:
        raise ValueError(f"Broswer {browser_name} is not supported")
    return driver