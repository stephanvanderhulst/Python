#for loops
ninjas = ['ryu','crystal','yoshi','ken']

#for ninja in ninjas[1:3]:
#    print(ninja)
#Enumerate can be given a start number!
for index, ninja in enumerate(ninjas, start=1):
    if ninja == "yoshi":
        print(f'Number {index}: {ninja} - he is a black belt')
        break
    else:
        print(f'Number {index}: {ninja}')

#find largest number in a list
list = [0,12,300,33,77,8]
largest_number = 0
for i in list:
    if i > largest_number:
        largest_number = i
print(largest_number)

#remove duplicate numbers from a list
numbers = [4,4,4,3,12,7,5,2,7]
print(numbers)
for i in numbers:
    if numbers.count(i) > 1:
        print(f'number {i} was found {numbers.count(i)} times in the list, removing one occurence!')
        numbers.remove(i)
print(numbers)

#convert digits of a phone number to words
phone = input('Type your phone number: ')
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#convert stuff to emojis
message = input(">")
words = message.split(' ')
emojis = {
    ":)":  "\U0001F600",
    ":D": "\U0001F603",
    ":(": "Don't be a sad cunt"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

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


#ranges
#for n in range(5):
#    print(n)

#for n in range(3,10):
#    print(n)

#for n in range(0,20,4):
#    print(n)

burgers = ['beef','chicken','veg','supreme','double']

#for n in range(len(burgers)):
#    print(n, burgers[n])

#go through array in reverse, step is -1 (third value)
for n in range(len(burgers) - 1,-1,-1):
    print(n,burgers[n])