def main(): 
    x = get_int()
    print(f"x is {x}")



def get_int(): 

    while True:
        try: 
            x = int(input("What is x? "))
    
        except ValueError: 
            print("x is not am integer")

        else:
            break
    
    return x   ## Or just omit the break and make it ELSE /n return x



main()