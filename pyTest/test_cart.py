import pytest


@pytest.fixture
def setUp():
    print("Launch the browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close the browser")

def testRemoveItemFromCart(setUp):
    print("Add Item Successfully")

def testAddItemtoCart():
    print("Remove Item Successfully")

