import pytest


@pytest.fixture
def setup():
    print("Open Browser")
    print("Login")
    yield
    print("Logout")

def test_add_item(setup):
    print("add Item")


def test_delete_item(setup):
    print("Delete Item")
