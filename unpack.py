## traditional unpacking

first, last = input("What is your name? ").split(" ")
print(f"Hello, {first}")

coins = [100, 50, 25]


def total(galleons, sickles, knuts): 
    return(galleons * 17 + sickles) * 29 + knuts

""" 
This is the verbose version of the code 

print(total(coins[0], coins[1], coins[2]), "knuts")

A better version of the code utilizing UNPACKING would be 
"""

"""
Unpacking the list with * will pass the individual values in the list
"""

print(total(*coins), "knuts")

print(coins)
"""
prints [100, 50, 25]
"""
print(*coins)
"""
prints 100 50 26   This means it passes the individual members of the list 
"""