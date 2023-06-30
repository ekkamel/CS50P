def main(): 
    name = input("What is your name? ")
    print(hello(name))


def hello(to="world"):     # this makes world a default 
    return f"hello, {to}"
    
    
if __name__ == "__main__":
    main()
    