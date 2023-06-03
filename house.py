name = input("What's your name? ")

match name: 
    case "Harry" | "Herminoe" | "Ron": 
        print("Gryffindor")    
    #case "Herminoe": 
    #    print("Gryffindor")
    #case "Ron": 
    #    print("Gryffindor")
    case "Draco": 
        print("Slytherin")
    case _:                 # Any other case 
        print("Who?")