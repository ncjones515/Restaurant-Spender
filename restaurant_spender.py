from pathlib import Path
import json

print("Welcome to the restaurant spender!")

while True:
    user_n = input("What is your name?")
    path = Path(f"{user_n}.json")
    if path.exists():
        print(f"Welcome back {user_n.title()}!")
        dict = path.read_text()
        user = json.loads(dict)
    else:
        print(f"Welcome to the restaurant tracker, {user_n.title()}!")
        user = {}
    while True:
        print("\nWhat would you like to do?:")
        print("1.Add meal, 2.Total spent, 3.Average spent, 4.View all meals, 5.Switch user")
        menu = input("Enter 1-5:")
        if menu == "1":
            while True:
                name = input("What is the name of the restaurant you ate at?")
                
                #Greeting
                print("Let's calculate the tip.")

                #Collect input
                bill = input("What was the total bill?")
                tip = input("How much tip would you like to give? 0, 10, 12, 15?")
                people = input("How many people to split the bill?")

                #Convert to integers
                bill = float(bill)
                tip = int(tip)
                people = int(people)
                
                #Calculation
                if tip == 0:
                    bill = bill * 1
                elif tip == 10:
                    bill = bill * 1.1
                elif tip == 12:
                    bill = bill * 1.12
                elif tip == 15:
                    bill = bill * 1.15
                
                split_cost = bill / people

                split_cost = round(split_cost, 2)

                user[name] = split_cost
                print(f"The cost per person is {split_cost}.")

                print("Would you like to enter another restaurant?")
                another = input("Type yes or no.")
                if another == 'no':
                    break
            
        elif menu == "2":
            total = 0
            for value in user.values():
                bill_1 = float(value)
                total  = total + bill_1
                
            print(f"\nYou have spent ${total} on restaurants.")

        elif menu == "3":
            total = 0
            quant = 0
            for value in user.values():
                value = float(value)
                quant += 1
                total = total + value
            avg = total / quant

            avg = round(avg, 2)

            print(f"You spend ${avg} on average at restaurants.")
        
        elif menu == "4":
            for key, value in user.items():
                print(key.title(),":", f"${value}")

        elif menu == "5":
            dict_1 = json.dumps(user)
            path.write_text(dict_1)
            break
