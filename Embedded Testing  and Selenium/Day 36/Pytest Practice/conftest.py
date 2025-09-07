# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new") # comment out to see browser
    options.add_argument("--window-size=1280,800")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()