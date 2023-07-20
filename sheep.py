def main(): 
    n = int(input("What is n? "))
    for s in sheep(n): 
        print(s)



"""
def sheep(n): 
    flock = []
    for i in range(n): 
        flock.append("sheep" * i)
    return flock

With big huge number, the computer stops returning anything 

"""

def sheep(n): 
    for i in range(n): 
        yield "sheep" * i     ## This is named Generator 


"""
This way will work even with big huge number of sheep 
This method runs one iteration, suspends, returns a value, then iterates...etc
"""


if __name__ == "__main__":
    main()