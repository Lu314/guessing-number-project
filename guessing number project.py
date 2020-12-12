import random 

def guess(x):
    random_number = random.randint(20,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f'Guess a number between 20 and {x}'))
        if guess < random_number:
            print('Sorry, guess again.Too low.')
        elif guess > random_number:
            print('Sorry, guess again.Too high.')

    print(f'Nice, congrats. You have guessed the right number {random_number}')

guess(40)
