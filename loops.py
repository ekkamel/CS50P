for i in range(5): 
    print("Meaw")

print("Meaw\n" * 4)

print("Meaw\n" * 4, end="")

# Loop till you get a positive number input 

while True:
    n=int(input("What's n? "))
    if n < 0: 
        continue
    else: 
        break

## OR 

while True:
    n=int(input("What's n? "))
    if n > 0: 
        break

## Write it in a function 

def main(): 
    number = get_number()
    meow(number)

def get_number(): 
    while True: 
        n = int(input("What's n? "))
        if n > 0: 
            break
    return n 

def meow(n): 
    for i in range(n): 
        print("Meaw")

main()
