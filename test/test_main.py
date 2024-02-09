import pytest

def returnietskeer9(x: int):
    return x * 9

def test_returnietskeer8(): 
    result = returnietskeer9(2)
    assert result == 14