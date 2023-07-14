def main(): 
    yell("This", "is", "CS50")
    yell_map("This", "is", "CS50")
    yell_list("This", "is", "CS50")


def yell(*args):                # or any name like *words
    uppercased = []
    for word in args: 
        uppercased.append(word.upper())
    print(*uppercased)    


def yell_map(*args): 
    uppercased = map(str.upper, args)           # No upper() cause I am not calling
    print(*uppercased)                          # the function, I am passing it
    

def yell_list(*args):
    uppercased = [arg.upper() for arg in args]
    print(*uppercased)
    print(uppercased)


if __name__ == "__main__":
    main()