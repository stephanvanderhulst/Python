#function with default parameters
#def greet(name = 'Ryu',time = 'morning'):
#    print(f'Good {time} {name}, hope you are well')

#greet()
#greet('shaun', 'morning')
#greet(time="afternoon")

def area(radius):
    return 3.14 * radius * radius

def volume(area, length):
    print(area * length)

volume(area(10),10)