def total(galleons, sickles, knuts): 
    return(galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}


print(total(**coins), "knuts")
"""
Note in unpacking a list  we used * 
in unpacking a Dict we use **
"""