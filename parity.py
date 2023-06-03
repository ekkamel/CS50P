def main(): 
    x = int(input('What is x? '))
    if is_even(x): 
        print("Even")
    else: 
        print("Odd")
    

def is_even(n):
    
## Actually this is all you need, because it will naturally return True or False     
    return n % 2 == 0
    

## One way of writing the function ...    
#    return True if n % 2 == 0 else False 


## One other way to write the same function would be....

#    if n % 2 == 0:
#        return True
#    else: 
#        return False



main()