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