class Account: 
    def __init__(self): 
        self._balance = 0        ## Initiate each account with 0 value
                                 ## the _ indicates the var should not be touched 
                                 ## by other functions
                                 
                                 ## This is called instance variable and it is reachable 
                                 ## anywhere within the class
                                 
    @property                    ## ensures the variable is not changed without a SETTER
    def balance(self):           ## this function is actually a GETTER
        return self._balance
    
    
    def deposit(self, n):
        self._balance += n 
    
    
    def withdraw(self, n):
        self._balance -= n
        

def main():
      account = Account()
      print("Balance:", account.balance)
      account.deposit(100)
      account.withdraw(50)
      print("Balance:", account.balance)
      
      
if __name__ == "__main__": 
    main()
      