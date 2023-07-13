import sys 

if len(sys.argv) == 1:     
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:     
    print("usage of meows.py")


"""
YOu can try this with py meow-argv.py -n 3
"""    