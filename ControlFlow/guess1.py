import random

number = random.randint(1, 25)

# number_of_guesses = 0

for i in range(5):
# while number_of_guesses < 5:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)

    # number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('You guessed the number!')

else:
    print('You did not guess the number. The number was ' + str(number))