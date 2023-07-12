class Cat:
    MEOWS = 3        ## capitalized vars are constants
    
    def meow(self): 
        for _ in range(Cat.MEOWS): 
            print("meow")
            
            
            
cat = Cat()
cat.meow()      