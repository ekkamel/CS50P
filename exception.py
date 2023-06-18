def main(): 
    x = get_int("What is x? ")
    print(f"x is {x}")



def get_int(prompt): 

    while True:
        try: 
            x = int(input(prompt))
    
        except ValueError: 
            # print("x is not am integer")
            pass

        else:
            break
    
    return x   ## Or just omit the break and make it ELSE /n return x



main()