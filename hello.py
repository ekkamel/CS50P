"""
This is a multiline 
comment 
"""

name = input("What is your name? ")
print("hello, ", end="")
print(name)

# Remove whitespace from string
name = name.strip()

## There is rstrip() and lstrip()


print(f"hello, {name}")

# capitalize the first letter
name = name.capitalize()
print(f"hello, {name}")

# capitalize the first letter of each word
name = name.title()
print(f"hello, {name}")

# We can also chain the methods
name = name.strip().title()
print(f"hello, {name}")

# you can also do this
# name = input("What is your name? ").strip().title()

# split the name into first name and last name
first, last = name.split(" ")
print(f"First name: {first}, Last name: {last}")
