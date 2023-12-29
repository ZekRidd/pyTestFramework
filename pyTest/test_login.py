import pytest

@pytest.mark.skip
def testLogin():
    print("Login Successfully")

@pytest.mark.regression
def testLogoff():
    print("Logoff Successfully")

@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 4

@pytest.mark.xfail
def testCalculation1():
    assert 2+2 == 5