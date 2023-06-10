students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


## OR 

for i in range(len(students)):
    print(students[i])

    ## or 
    print(i, students[i])


## Dictionaries 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

print(students["Hermione"])

## OR 
for student in students: 
    print(student)          # This returns KEYS


for student in students: 
    print(student, students[student])  ## This prints KEYS and VALUES

    ## You can beautify this 
    print(student, students[student], sep = ",") 

## We can build a LIST of DICTIONARIES if the structure is more complicated

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Draco", "house": "Gryffindor", "patronus": None}
]

for student in students: 
    print(student["name"], student["house"], sep=", ")        #print name, house
