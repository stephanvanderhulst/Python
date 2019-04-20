#while loops
age = 25
num = 0

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1

secret_number = 9
guess_count = 0
guess_limit
while guess_count < guess_limit:
    guess = input('Guess the secret number : ')
    if int(guess) == secret_number:
        print('You win!')
        break
    else:
        print('wrong!')
    guess_count += 1

#car game
while True:
    user_input = input('>')

    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif user_input == 'start':
        print('The car has started moving')
    elif user_input == 'stop':
        print('The car has stopped moving')
    elif user_input == 'quit':
        break