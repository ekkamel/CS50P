def meow(n: int) -> str: 
    """
    Meow n times.

    :param n: number of times to meow
    :type n: int
    :raise TypeError: if n is not int
    :return: A string of n meows, one per line 
    :rtype: str
    """
    
    for _ in range(n): 
        print("meow")
        
number = input("number: ")
meow(number)

## this module is done to test mypy
## I hinted that n needs to be int in line 1 
## then I can run mypy meows2.py 
## and it will me that line 6 is passing an incompatble type (str) 