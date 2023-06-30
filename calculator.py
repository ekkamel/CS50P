def main(): 
    x = int(input("What is x? "))
    print("x squared is", square(x))


def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)     ## These are all the same 


if __name__ == "__main__":
    main()