def meow(n: int): 
    for _ in range(n): 
        print("meow")
        
number = input("number: ")
meow(number)

## this module is done to test mypy
## I hinted that n needs to be int in line 1 
## then I can run mypy meows2.py 
## and it will me that line 6 is passing an incompatble type (str) 