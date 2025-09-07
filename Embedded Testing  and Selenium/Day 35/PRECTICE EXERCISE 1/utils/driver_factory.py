from selenium import webdriver

def driver_factory(browsers):
    if browsers.lower()=='chrome':
        return webdriver.Chrome()
    elif browsers.lower()=='firefox':
        return webdriver.Firefox()
    elif browsers.lower()=='edge':
        return webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browsers}. Supported browsers are Chrome, Firefox, and Edge.")
    