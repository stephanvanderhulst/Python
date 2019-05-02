#for loops
ninjas = ['ryu','crystal','yoshi','ken']

#for ninja in ninjas[1:3]:
#    print(ninja)

for ninja in ninjas:
    if ninja == "yoshi":
        print(f'{ninja} - he is a black belt')
        break
    else:
        print(ninja)

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