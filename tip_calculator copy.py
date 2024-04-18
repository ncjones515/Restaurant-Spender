from pathlib import Path
import json

#Find the list file, and read it into memory
path = Path('list.json')
list = path.read_text()
list = json.loads(list)

#Checks the list from the json file, to see if the user is new or returning
u_name = input("What is your name?")
if u_name in list:
    print(f"Welcome back, {u_name.title()}!")
    n_path = Path(f"{u_name}.json")
    d = n_path.read_text()
    dict = json.loads(d)
else:
    list.append(u_name)

    print(f"Welcome to the restaurant tracker, {u_name.title()}!")



name = input("What is the name of the restaurant you ate at?")

while True:  
    #Greeting
    print("Let's calculate the tip.")

    #Collect input
    bill = input("What was the total bill?")
    tip = input("How much tip would you like to give? 10, 12, 15?")
    people = input("How many people to split the bill?")

    #Convert to integers

    bill = float(bill)
    tip = int(tip)
    people = int(people)

    #Calculation

    if tip == 10:
        bill = bill * 1.1
            
    elif tip == 12:
        bill = bill * 1.12
            
    elif tip == 15:
        bill = bill * 1.15
            

    split_cost = bill / people

    print(f"The cost per person is {split_cost}.")

    print("Would you like to enter another restaurant?")
    another = input("Type yes or no.")
    if another == 'no':
        break

