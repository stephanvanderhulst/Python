#function that converts a decimal number to binary
import math #So we can use the floor function

def decimalToBinary(decimal):
    print(f'Converting decimal {decimal} into a binary number')
    binary = ""
    while decimal > 0:
        print(f'Divide {decimal} by 2 ({decimal/2}), floor it to {math.floor(decimal/2)} and store the modulus of {decimal % 2}')
        binary = str(decimal % 2) + binary
        decimal = math.floor(decimal/2)
        print(binary)


#decimalToBinary(1218)
#print(bin(1218))

#Test a number to see if it is a prime number
def verifyPrime(candidate):
    lower_bound = 2
    upper_bound = int(math.sqrt(candidate))
    print(f'To determine if {candidate} is a prime number we will divide it by the numbers from 2 to {upper_bound} (floor of the square root of {candidate})')
    while lower_bound < upper_bound:
        lower_bound += 1
        if candidate % lower_bound == 0:
            print(f'{candidate} is NOT a prime number because it is the multiplication of {lower_bound} and {int(candidate/lower_bound)}')
            return
    print(f'{candidate} IS a prime number because it could not be divided by any number from 2 to {upper_bound}')


#verifyPrime(11233)
#verifyPrime(17321)

# O(n)
def fibonacciSequence(sequence_length):
    fibonacci = [0]
    for x in range(1, sequence_length):
        if len(fibonacci) < 2:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[x-1] + fibonacci[x-2])
    print(fibonacci)

#print('[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] is our test sequence')
#fibonacciSequence(23)


#now a function that gives the fibonacci number at a certain position
def fibonacciNumber(position):
    if position == 0 or position == 1: return 1
    nums = position+1
    nums[0] = 1
    nums[1] = 1
    for i in range[2:position]:
        nums[i] = nums[i-1] + nums[i-2]
    return nums[position]

print(fibonacciNumber(5))


#Find count of an element in a sorted list: O(n) solution
def findElementCount(sorted_list, element):
    count = 0
    for step in sorted_list:
        if step == element:
            count += 1
        elif step > element: #making it a little bit faster
            break
    print(count)


#findElementCount([1,1,3,3,5,5,5,5,5,9,9,11], 5)


def middleOfList(list):
    return math.floor(len(list)/2)

#now lets use binary search to find any occurence of element in the sorted list
def findAnyOccurence(sorted_list, element):
    print(sorted_list)
    midway = middleOfList(sorted_list)
    while sorted_list[midway] != element:
        if sorted_list[midway] > element:
            print(f'any occurence of {element} is to the left of position {sorted_list[midway]} in the list')
            #delete the right half of the list
            del(sorted_list[midway:])
            print(f'Deleted the right half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)
        elif len(sorted_list) == 1:
            print(f'Element {element} has not been found in the list')
            break
        else:
            print(f'any occurence of {element} is to the right of position {sorted_list[midway]} in the list')
            #delete the left half of the list
            del(sorted_list[:midway])
            print(f'Deleted the left half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)

    print(f'an occurence of {element} is at position {sorted_list[midway]} in the list')


#findAnyOccurence([1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11], 4)


#now lets use binary search to find first occurence of element in the sorted list
def findFirstOccurence(sorted_list, element):
    print(sorted_list)
    midway = middleOfList(sorted_list)
    while True:
        if sorted_list[midway] > element:
            print(f'First occurence of {element} is to the left of position {sorted_list[midway]} in the list')
            #delete the right half of the list
            del(sorted_list[midway:])
            print(f'Deleted the right half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)
        elif len(sorted_list) == 1:
            print(f'Element {element} has not been found in the list')
            break
        elif sorted_list[midway] == element:
            print(f'an occurence of {element} is at position {sorted_list[midway]} in the list')
            #delete the right half of the list
            del(sorted_list[midway:])
            print(f'Deleted the right half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)
        elif sorted_list[-1] == element and sorted_list[-2] != element:
            print(f'First occurence of {element} is at position {len(sorted_list)-1} in the list')
            break
        else:
            print(f'First occurence of {element} is to the right of position {sorted_list[midway]} in the list')
            #delete the left half of the list
            del(sorted_list[:midway])
            print(f'Deleted the left half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)


#findFirstOccurence([1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11], 3)


def findLastOccurence(sorted_list, element):
    print(sorted_list)
    midway = middleOfList(sorted_list)
    while True:
        if sorted_list[midway] > element:
            print(f'Last occurence of {element} is to the left of position {sorted_list[midway]} in the list')
            #delete the right half of the list
            del(sorted_list[midway:])
            print(f'Deleted the right half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)
        elif len(sorted_list) == 1:
            print(f'Element {element} has not been found in the list')
            break
        elif sorted_list[midway] == element:
            print(f'an occurence of {element} is at position {sorted_list[midway]} in the list')
            #delete the left half of the list
            del(sorted_list[:midway])
            print(f'Deleted the left half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)
        elif sorted_list[0] == element and sorted_list[1] != element:
            print(f'Last occurence of {element} is at position {len(sorted_list)-1} in the list')
            break
        else:
            print(f'Last occurence of {element} is to the right of position {sorted_list[midway]} in the list')
            #delete the left half of the list
            del(sorted_list[:midway])
            print(f'Deleted the left half of the list, new list is: {sorted_list}')
            #find the new midway
            midway = middleOfList(sorted_list)


#findLastOccurence([1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11], 3)
#eventually I want a function that will take an array en I can request any occurence, first occurence, last occurence or the count of element

#mycodeschool implementation of firstoccurence and lastoccurence:
def binarySearch(list, element):
    listLength = len(list)
    low = 0
    high = listLength
    result = -1
    while(low <= high):
        mid = (low+high)/2
        if element == list[middleOfList(list)]:
            result = middleOfList(list)
            high = middleOfList(list)-1 #this becomes low = middleOfList(list)+1 if we want last occurence
        elif element == list[middleOfList(list)]:
            high = middleOfList(list)-1
        else:
            low = middleOfList(list)+1
    print(result)

#Nice video! I would suggest calculating 'mid' index this way:
#min <- low + (high - low) / 2
#to avoid integer overflow on large arrays.﻿

#this currently is an endless loop
#binarySearch([1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11], 3)


# def maximumSubarrayProblem():
#     the_array = [1,-3,2,1,-1]
#     maxSubarray loop door array vanaf begin
#     loop for array length
#         possibleMax += [i]
#         if possibleMax < 1 (waar we eigenlijk mee starten)
#             nieuwe poging possibleMax = 0
#         is huidig totaal het hoogste wat we ooit hebben gehaald?
#         alltimehigh
#             if (possibleMax > allTimeHigh):
#                 allTimeHigh = possibleMax
#                 hoe gaan we start en eind positie vinden?
#         3 return values: startposition, endposition en maxcount
#
# python libraries
#     numpy
#     pandas
#     matplotlib
#     scikit-learn


#FizzBuzz cleaner method that can easily be expanded
def fizz_buzz(game_length):
        for i in range(game_length):
                output = ""

                if(i % 3 == 0): output += "Fizz"
                if(i % 5 == 0): output += "Buzz"
                if(output == ""): output = i + 1

                print(output)


#fizz_buzz(30)

total_numbers = 0

for number in range(1,10):
    if number %2 == 0:
        print(number)
        total_numbers += 1
print(f"We have {total_numbers} even numbers")