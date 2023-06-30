name = input("What is your name? ")

with open("names.txt", "a") as file: ## creats the file if not existing
    file.write(f"{name}\n")
    

## In opening a file with "w" it is re-created and re-written 
## open with "a" to "Append" 