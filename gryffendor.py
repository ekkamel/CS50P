students = [
    {'name': 'Hermione', 'house': 'Gryffendor'}, 
    {'name': 'Harry', 'house': 'Gryffendor'},
    {'name': 'Ron', 'house': 'Gryffendor'},
    {'name': 'Draco', 'house': 'Slytherin'},
    {'name': 'Padma', 'house': 'Ravenclaw'},
]

gryffendors = [
    student["name"] for student in students if student["house"] == 'Gryffendor'
]

for gryffendor in sorted(gryffendors):
    print(gryffendor) 


def is_gryffendor(s):
    return s["house"] == 'Gryffendor' 
    
gryffendorss = filter(is_gryffendor, students)

"""
you can eliminate the is_gryffendor function by doing this 

gryffendorss = filter(lambda s: s["house"] == 'gryffendor', students)
"""

for g in gryffendorss: 
    print(g["name"])


"""
to make it sorted 
for g in sorted(gryffendorss, key=lambda s: s["name"]): 
"""