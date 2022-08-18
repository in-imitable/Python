import random

secret_number = random.randint(1, 20)

print("I'm thinking a number between 1 to 20")

for guesses_taken in range(1, 7):
    print('Guess the number: ')
    guess = int(input())

    if guess > secret_number:
        print('Your guess is too high')

    elif guess < secret_number:
        print('Your guess is too low')

    else:
        break

if guess == secret_number:
    print(f'You Won! You guess my number in {guesses_taken} guesses.')

else:
    print(f'Nope. The number I was thinking of was {secret_number}')
