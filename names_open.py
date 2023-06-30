names = []

with open("names.txt", "r") as file: 
    for line in sorted(file, reverse=True):
        print(f"{line.rstrip()}")   ## This removes the extra new line

## or 
## for name in sorted(names):
## print......