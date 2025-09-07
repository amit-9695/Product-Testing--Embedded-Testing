from utils import is_strong_password

def test_strong_password():
    assert is_strong_password("MyPass123786$")
    print("This password is strong.")

def test_weak_password_short():
    assert not is_strong_password("M1!")
    print("This password is too short.")

def test_weak_password_no_digit():
    assert not is_strong_password("MyPassword!")
    print("This password is missing a digit.")

def test_weak_password_no_upper():
    assert not is_strong_password("mypassword1!")
    print("This password is missing an uppercase letter.")

def test_weak_password_no_special():
    assert not is_strong_password("MyPassword1")
    print("This password is missing a special character.")
    