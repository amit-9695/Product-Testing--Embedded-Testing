from utils import is_valid_email

def test_valid_email():
    assert is_valid_email("test@example.com")

def test_invalid_email_no_at():
    assert not is_valid_email("test.example.com")

def test_invalid_email_no_domain():
    assert not is_valid_email("test@")

def test_valid_email_with_dash():
    assert is_valid_email("user-name_123@mail.couk")
