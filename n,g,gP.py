import random

computer = random.randint(1,100)
tires = 0

print("I choose a nubmer between 1 to 100, Now your turn...")

while True:
    try:
        guess = int(input("Guess the nubmer : "))
        tires += 1

        if guess > computer:
            print("Choose small number please...")
        elif guess < computer:
            print("Choose big number please...")
        else:
            print(f"Congrats, right guess you did it in {tires}")
            break

    except ValueError:
        print("Invalid input please enter number only...")
    
