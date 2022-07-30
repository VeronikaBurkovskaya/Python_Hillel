import random

i = 1
while i < 4:
    number_user = input("Enter your number from 0 to 10")
    number_system = random.randint(0,10)
    print("You WIN =)" if number_system == number_user else "You LOSE =(")
    i += 1