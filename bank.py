balance = 0 

def main(): 
    deposit(100)
    withdraw(50)
    print("balance:", balance)
    

def deposit(n): 
    global balance      ### I needed to call it GLOBAL to make it access the var
    balance += n        ## changing a Global variable inside a function doesn't work


def withdraw(n): 
    global balance
    balance -= n

    
if __name__ == "__main__":
    main() 
