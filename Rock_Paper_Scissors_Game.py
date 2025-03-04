# %%
# Rock Paper Scissiors Game


import random as rn

while True: 
    choices = ["rock","paper", "scissors"]
    player = None

    computer = rn.choice(choices)

    while player not in choices:
        player = input("Rock, Paper, Scissors?: ").lower()

    if player == computer:
        print("Computer: "+computer)
        print("Player: "+ player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You loose!")
        if computer == "scissors":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You loose!")
        if computer == "paper":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You loose!")
        if computer == "rock":
            print("Computer: "+computer)
            print("Player: "+ player)
            print("You Win!")
    
    play_again=input("Play again? (yes/no)?: ").lower()

    if play_again != "yes":
        break
    
print("Thank you for playing.")
