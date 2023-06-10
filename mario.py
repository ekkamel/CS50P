## go vertical

def main(): 
    print_column(3) 

def print_column(height):
    print("#\n" * height, end="")


main()


## go horizontal 

def main(): 
    print_row(4)


def print_row(width):
    print("?" * width)

main()


## go square 
def main(): 
    print_square(3)


def print_square(size): 
    # for each row in square 
    for i in range(size): 
        #for each brick in row 
        for j in range(size):
            #print brick 
            print("#", end="")
        # jumps to a new line (row)
        print()

