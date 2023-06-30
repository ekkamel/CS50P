import pytest

from calculator import square 


def test_square(): 
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4

def test_zero(): 
    assert square(0) == 0

def test_str(): 
    with pytest.raises(TypeError):
        square("cat")


## You need to 
## pip install pytest 
## run this code as follows 
## pytest test_calc2.py

## for the pytest to work, a function must be RETURNING value
