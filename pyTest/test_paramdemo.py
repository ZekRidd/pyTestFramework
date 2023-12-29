import pytest


@pytest.mark.parametrize("a,b,final",[(2,4,6),(3,4,7),(5,10,13)])
def test_add(a,b,final):
    assert a+b==final