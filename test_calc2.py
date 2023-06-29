from calculator import square

def test_square(): 
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4

## YOu need to 
## pip install pytest 
## run this code as follows 
## pytest test_calc2.py

