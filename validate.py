import re

def main(): 
    #no_regex()
    with_regex()

def no_regex(): 
    email = input("Whatis your email? ").strip()

    username, domain = email.split("@")

    if username and domain.endswith(".edu"): 
        print("valid")
    else: 
        print("invalid")


def with_regex():
    email = input("Whatis your email? ").strip()

    if re.search(r"^.[^@]+@.+\.edu$", email):  # repition of characters right and left
        print("valid")                     # note the \
    else:                                  # r means raw string
        print("invalid")



if __name__ == "__main__":
    main()


## .     any character except a newline 
## *     0 or more repetitions
## +     1 or more repetitions
## ?     0 0r 1 repetion 
## {m}   m repitions 
## {m,n} m-n repitions
## ^     matches the start of the string 
## $     matches the end of the string right before the newline