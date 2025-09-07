import pytest

@pytest.fixture
def config():
    return {"env":"dev"}

@pytest.fixture
def db(config):
    return f" {config['env']}_db"

@pytest.fixture
def app(db):
    return f"web_app_using_{db}"

def test_app(app):
    assert "web_app_using" in app

# test_app(app)-->aap(db)-->db(config)->