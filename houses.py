students = [
    {'name': 'Hermione', 'house': 'Gryffendor'}, 
    {'name': 'Harry', 'house': 'Gryffendor'},
    {'name': 'Ron', 'house': 'Gryffendor'},
    {'name': 'Draco', 'house': 'Slytherin'},
    {'name': 'Padma', 'house': 'Ravenclaw'},
]

## How to get a list of the unique houses

houses = []
for student in students: 
    if student['house'] not in houses: 
        houses.append(student['house'])

for house in sorted(houses): 
    print(house) 


## another way is through using SET 

houses = set()
for student in students: 
    houses.add(student['house'])

for house in sorted(houses): 
    print(house) 