import random
while True:
    choices = ["rock", "paper", "scissor"]
    player = "gaurav"
    while player not in choices:
        player = input("rock, paper, scissor : ").lower()
    computer = random.choice(choices)
    if player == computer:
        print("computer : ", computer)
        print("player : ", player)
        print("It's a Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("computer : ", computer)
            print("player : ", player)
            print("you lose")
        if computer == "scissor":
            print("computer : ", computer)
            print("player : ", player)
            print("you win")
    elif player == "paper":
        if computer == "scissor":
            print("computer : ", computer)
            print("player : ", player)
            print("you lose")
        if computer == "rock":
            print("computer : ", computer)
            print("player : ", player)
            print("you win")
    elif player == "scissor":
        if computer == "rock":
            print("computer : ", computer)
            print("player : ", player)
            print("you lose")
        if computer == "paper":
            print("computer : ", computer)
            print("player : ", player)
            print("you win")
    print("----------------------------------------------------")
    play_again = input("Do you want to play again(yes/no or y/n): ").lower()
    if play_again != "yes":
        if play_again != "y":
            break
print("Bye!!!")
