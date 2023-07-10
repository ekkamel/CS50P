import random

class Hat: 
    #def __init__(self):  ## no need to initiate a @classmethod
                          ## no need to use self as well
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod    
    def sort(cls, name):        ## we use cls and not self in @classmethod
        print(name, "is in", random.choice(cls.houses))    


#hat = Hat()             ## inistantiate class 
                         ## No need for inistantiation with @classmethod
Hat.sort("Harry")