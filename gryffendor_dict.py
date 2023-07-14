"""
Creating dictionary in the fly
This is called Dictionary Comprehension
"""

students = ["Hermione", "Harry", "Ron"]

gryffendors = {student: "Gryffendor" for student in students}

print(gryffendors)


"""
Enumeration

"""

for i, student in enumerate(students):
    print(i + 1, student)