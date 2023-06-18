import sys 

if len(sys.argv) < 2: 
    sys.exit("too few arguments")

for arg in sys.argv[1:]:   ## cause I need to skip element 0
    print("hello my name is", arg)
