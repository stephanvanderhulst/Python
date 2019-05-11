#age = int(input("Your age is: "))

#if age > 30:
#    print("you are over 30 lmao!!")
#elif age >20:
#    print("You are under 30 but over 20 wtf")
#else:
#    print("You are under 10 wtf")

meaty = input("Do you eat meat? (y/n): ")

if meaty != 'n':
    print("Nice to meat you hehehe")
else:
    print("Get out vegan scum!")


good_credit = False
house_price = 1_000_000

if good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f'The down payment is: {down_payment:,}')