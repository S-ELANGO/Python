import random

choices = ['rock', 'paper', 'scissor']

while True:
    computer_choice = random.choice(choices)
    player_choice = input('Enter your choice (rock, paper, scissor): ').lower()

    if player_choice not in choices:
        print('❌ Invalid choice. Try again.')
        continue

    print('Computer chose:', computer_choice)

    if player_choice == computer_choice:
        print('🤝 It’s a tie')
    elif (
        (player_choice == 'rock' and computer_choice == 'scissor') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissor' and computer_choice == 'paper')
    ):
        print('🎉 You win!')
    else:
        print('💻 Computer wins!')

    break
