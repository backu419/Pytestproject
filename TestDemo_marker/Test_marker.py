import pytest
import sys


@pytest.mark.smoke
def test_login():
    print("Login Details")


@pytest.mark.regression
def test_add_item():
    print("Adding Item to the Cart")


@pytest.mark.skip
def test_checkout():
    print("Checkout")


@pytest.mark.smoke
@pytest.mark.regression
def test_logout():
    print("Logout")


@pytest.mark.skipif(sys.version_info < (3,12),reason="will execute above python 3.11 version ")
def test_demo():
    print("Demo skipif ")
