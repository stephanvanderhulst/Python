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


decimalToBinary(1218)
print(bin(1218))

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


verifyPrime(11233)
verifyPrime(33216)


def fibonacciSequence():
    example = [1,1,2,3,5,8,13,21,34,55,89,144,233]
    print(f'Fibonacci sequence: {example}')


fibonacciSequence()


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