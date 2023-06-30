def main():
    print_unsorted()
    print_sorted()
    create_dict()


def print_unsorted():    
    with open("students.csv") as file: 
        for line in file:
            # row = line.rstrip().split(",")   This is one way 
            # print(f"{row[0]} is in {row[1]}")
        
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}") 


def print_sorted(): 
    students  = []
    with open("students.csv") as file: 
        for line in file: 
            name, house = line.rstrip().split(",")
            students.append(f"{name} lives in {house}")
        
        for student in sorted(students):
            print(student)


def create_dict(): 
    students = []
    with open("students.csv") as file: 
        for line in file: 
            name, house = line.rstrip().split(",")
            student = {}
            student["name"] = name 
            student["house"] = house
            ## or student = {"name": name, "house": house}
            students.append(student)
    
    for student in students: 
        print(f"{student['name']} is in {student['house']}")







if __name__ == "__main__":
    main()