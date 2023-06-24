def main(): 
    hello("world")
    goodbye("world")


def hello(name): 
    print(f"hello, {name}")


def goodbye(name): 
    print(f"goodbye, {name}")


## Do not call main() unconditionally, use this technique instead 
## this way if I run the code from command line it will print the 
## Hello and Goodbye world
## however, if called from another prgram will rin only the parameter
## that is passed to it
if __name__ == "__main__":
    main()