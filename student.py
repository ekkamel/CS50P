class Student:
    def __init__(self, name, house):    ## adding variables to objects 
        if not name: 
            raise ValueError("Missing name")        
        self.name = name 
        self.house = house
        #self.patronus = patronus
        
    def __str__(self): 
        return f"{self.name} from {self.house}"
    
    # getter 
    @property
    def house(self): 
        return self._house
    
    # setter
    @house.setter
    def house(self, house): 
        if house not in ["Gryffendor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Invalid house")
        self._house = house
    
    
    def charm(self): 
        #match self.patronus        only in Pyhton 3.10 
        if self.patronus == 'Stag': 
            return "Pizza"
        elif self.patronus == 'Otter': 
            return 'another emoji'
    
    @classmethod    
    def get(cls):     
        name = input("name: ")
        house = input("house: ")
        patronus = input("patronus: ")
        return cls(name, house)     ## here I passed the calss name as afunction 
                                        ## This line is a constructor call
                                        ## This line CONSTRUCTS a Student object for me 
                                        ## another name is INSTANTIATION 
                                    
                                        ## This calls the __init__ fuction
        

def main():    
    #name, house = get_student()
    
    #student = get_student()
    #if student[0] == "Padma": 
    #    student[1] = "Ravenclaw"
    #print(f"{student[0]} from {student[1]}")

    student = Student.get()    
    print("Expecto Patronum!")
    print(student.charm())
    
    


def get_student(): 
    name = input("name: ")
    house = input("house: ")
    return [name, house]       # you can separate the two variables
                               # or combine them in () as a TUPLE (non-mutable)
                               # or in [] as alist (mutable)

    
def get_student_dict():     
    name = input("name: ")
    house= input("house: ")
    return {"name": name, "house": house}   ## Returning a dictionary


  

if __name__ == "__main__":
    main()