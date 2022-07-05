from calendar import c
import imp


import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if (computer_choice > choice):
    print("Computer Wins!")
elif (computer_choice == choice):
    print("Nobody wins!")
elif (choice > computer_choice):
    print("YOU WIN!")
else:
    print("error!")
