import random

option = ["rock","paper","scissor"]
user = input("Choose one (rock,paper,scissor) : ").lower()
computer = random.choice(option)
print(f"Computer choose : {computer}")


if user == computer:
    print("Draw")
elif user == "rock":
    if computer == "scissor":
        print("You Win!")
    else:
        print("Computer Win!")
elif user == "paper":
    if computer == "rock":
        print("You Win!")
    else:
        print("computer Win!")
elif user == "scissor":
    if computer == "paper":
        print("You Win!")
    else:
        print("Computer Win!")
else:
    print("Wrong input....please enter only (rock,paper,scissor)...")
