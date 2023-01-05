import pytest

#@pytest.fixture(autouse=True)
#@pytest.fixture(scope="function",autouse=True)
#@pytest.fixture(scope="session",autouse=True)
@pytest.fixture(scope="module",autouse=True)
def setup():
    print("Open Browser")
    print("Login")
    yield
    print("Logout")