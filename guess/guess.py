import random

# randomly set a number between 1 and 10
answer = random.randint(1, 10)
prompt = 'Guess a number between 1 and 10: '
guesses = 0
guess = -1
user_guessed_correctly = False

while not user_guessed_correctly:
    user_input = input(prompt)
    if (user_input.isnumeric()): 
        guess = int(user_input)
        guesses += 1
        if (guess < answer):
            print ('Higher')
        elif (guess > answer):
            print ('Lower')
        elif (guess == answer):
            print ('Correct!')
            user_guessed_correctly = True
    else:
        print('That wasn\'t a number!  Try again!')



print(f'Congrats you got it in {guesses} guesses!')
