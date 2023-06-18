import sys 

try:
    print("hello, my name is", sys.argv[1])
except IndexError: 
    print("too few arguments")


if len(sys.argv) < 2: 
    sys.exit("too few arguments")
elif len(sys.argv) > 2: 
    sys.exit("too many arguments")

## of I get to this line, I know argv has the right number of items
print("hello, my name is", sys.argv[1])
