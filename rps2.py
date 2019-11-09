#Having another go with RPS.. Lost in first code

import random

rps = ["rock","paper","scissors"]
cpu = rps[random.randint(0,2)]

#Welcome and input
play_again = "yes"
while (play_again == "yes"): #While loop to keep playing
    if (play_again == "no"): #If you want to quit
        break
    print("\nWelcome to Rock Paper Scissors! ")
    print("\nPlease chose from the followingrock, paper, scissors")
    user = input("")

    #If statements
    if user == "rock":
        if cpu == "rock":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You tie!")
        elif cpu == "scissors":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You win!")
        elif cpu == "paper":
                print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You lose!")
    if user == "paper":
        if cpu == "rock":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You win!")
        elif cpu == "scissors":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You lose!")
        elif cpu == "paper":
                print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You tie!")
    if user == "scissors":
        if cpu == "rock":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You lose!")
        elif cpu == "scissors":
            print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You tie!")
        elif cpu == "paper":
                print(f"\nYou have chosen {user} and your oponent has chosen {cpu} You win!")
    else:
        print("Please play again.")

    play_again = input("Do you want to play again?")
    print("")
