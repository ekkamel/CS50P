from hello_function import hello

def test_default(): 
    assert hello() == "hello, world"  

def test_argument():
    assert hello("David") == "hello, David" 

## You must add __init__.py file to this directory 
## you can just run pytest test to runn all tests in this directory