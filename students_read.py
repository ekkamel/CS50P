import csv 

def main():
    #print_unsorted()
    #print_sorted()
    #create_dict()
    #lambda_function()
    #use_csv_module()
    #use_csv_dictreader()
    #write_csv()
    dict_write()

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
            name, house, score = line.rstrip().split(",")
            student = {}
            student["name"] = name 
            student["house"] = house
            student["score"] = score
            ## or student = {"name": name, "house": house, "score": score}
            students.append(student)    
    
        
        ## to sort on the house (use it as KEY for sorting)

        def get_score(student): 
            return int(student["score"])

        for student in sorted(students, key=get_score, reverse=True): 
            print(f"{student['name']} is in {student['house']} with score {student['score']}")


def lambda_function(): 
    students = []
    with open("students.csv") as file: 
        for line in file: 
            name, house, score = line.rstrip().split(",")
            student = {}
            student["name"] = name
            student["house"] = house
            student["score"] = score
            students.append(student)

        for student in sorted(students, key=lambda student: int(student["score"])):
            print(f"{student['name']} lives in {student['house']} with score {student['score']}")

        ## student: is not the name, lambda functions do not have names
        ## student: is the entity that the function is working on 
        ## student: is the function parameter

def use_csv_module():
    students = []
    with open("students2.csv") as file: 
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "score": int(row[1]), "home": row[2]})

        for student in sorted(students, key=lambda student: int(student["score"])): 
            print(f"{student['name']} lives in {student['home']} with score {student['score']}")     


def use_csv_dictreader():
    students = []
    with open("students3.csv") as file: 
        reader = csv.DictReader(file)  ## Note the first row in the csv file
        for row in reader: 
            students.append({"name": row["name"], "home": row["home"]})
        
        for student in sorted(students, key=lambda student: student["name"]): 
            print(f"{student['name']} lives in {student['home']}")     

def write_csv(): 
    name = input("What's your name? ")
    home = input("What's your home? ")

    with open("students4.csv", "a") as file: 
        writer = csv.writer(file)
        writer.writerow([name, home])


def dict_write(): 
    name = input("What's your name? ").strip()
    home = input("What's your home? ").strip()

    with open("students4.csv", "a") as file: 
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()