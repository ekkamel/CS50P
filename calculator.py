def main(): 
    x = int(input("What is x? "))
    print("x squared is", spuare(x))


def spuare(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)     ## These are all the same 


main()