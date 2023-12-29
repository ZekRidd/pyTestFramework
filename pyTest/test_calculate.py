import pytest


def testLogin():
    print("Login Successfully")

@pytest.mark.sanity
def testLogoff():
    print("Logoff Successfully")

def testCalculation():
    assert 2+2 == 4