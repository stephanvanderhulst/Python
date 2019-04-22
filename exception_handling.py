#exception handling
try:
    age = int(input('type your age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Zero div error')
except ValueError:
    print('stop doing that')