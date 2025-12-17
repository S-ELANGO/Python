import random
random_number=random.randint(1,100)
attempts=0

while True:
    guess= int(input("Enter your guess: "))
    attempts+=1

    if guess == random_number:
        print(f"Congrats! You guessed the number in {attempts} attempts.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


print('Thanks for playing')        
        