"""
The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
 * within 10 of the number, return "WARM!"
 * further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is
 * closer to the number than the previous guess return "WARMER!"
 * farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

"""

from random import randint

rand_num = randint(1,100)
guess_list=[]

# check the numbers insert by the user
while True:
    guess = int(input('Enter the number: '))
    guess_list.append(guess)
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
    elif guess == rand_num:
        print(f'You guessed correctly: {guess}, it took you {len(guess_list)} guesses')
        break
    elif len(guess_list) <= 1:
        if abs(rand_num - guess) <= 10:
            print('WARM')
        else:
            print('COLD')
    elif abs(rand_num - guess_list[-2]) > abs(rand_num - guess_list[-1]):
        print('WARMER')
    else:
        print('COLDER')