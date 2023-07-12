def meow(n: int) -> None: 
    for _ in range(n): 
        print("meow")
        

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

## testing this module with mypy will tell me that 
## there is an issue in line 7 as 
## "meow" does not return a value
## which is indicated by line 1