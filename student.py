def main():    
    #name, house = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student(): 
    name = input("name: ")
    house = input("house: ")
    return (name, house)       # you can separate the two variables
                               # or combine them in brackets as a TUPLE


if __name__ == "__main__":
    main()