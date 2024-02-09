import pytest

def returnietskeer7(x: int):
    return x * 7

def test_returnietskeer8(): 
    result = returnietskeer7(2)
    assert result == 14