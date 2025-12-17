import random

while True:
    input("Press enter to roll the dice")
    result = random.randint(1,6)
    print(f'the dice shows {result}')
    again=input('Roll again (y/n)')
    if again.lower() !='y':
        break
print('Thanks for playing')

