import random

random_n = random.randint(1, 5)
# print(random_n)

guess = input('please guess what is the number: \n')
print(f'your guess is: {guess}, type: {type(guess)}')

game = True
while game:
    if guess == 'exit':
        game = False
    else:
        if int(guess) == random_n:
            print('your guess is right!')
            game = False
        else:
            print('try again')
            guess = int(input('please guess what is the number: \n'))
            print(f'your guess is: {guess}, type: {type(guess)}')
            print(f'number is: {random_n}')

print('exit game')
