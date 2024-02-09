import pytest

def returnietskeer8(x: int):
    return x * 8

def test_returnietskeer8(): 
    result = returnietskeer8(2)
    assert result == 16