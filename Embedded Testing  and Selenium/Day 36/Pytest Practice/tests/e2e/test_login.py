import csv
import pathlib
import pytest
from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

DATA_FILE = pathlib.Path(__file__).parent / "data" / "users.csv"

def load_users():
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [ (row["username"], row["password"], row["expect_success"], row["expect_message"]) for row in reader ]
    
@pytest.mark.smoke
@pytest.mark.parametrize("username,password,expect_success,expect_message", [
    ("locked_out_user", "secret_sauce", 0, "Sorry, this user has been locked out.")
])
def test_login_flows(driver, base_url, username, password, expect_success,
expect_message):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(username, password)
    if int(expect_success):
        inv = InventoryPage(driver)
        assert inv.is_loaded(), "Inventory page should load on successful login"
    else:
        assert expect_message in login.error_text()