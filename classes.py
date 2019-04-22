class Point:
    def __init__(self, x, y): #constructor initialized
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is now talking')


person = Person("Jack")
person.talk()



class Mammal:
    def walk(self):
        print("walk")


#dog inherits walk method from mammal
class Dog(Mammal):
    def bark(self):
        print("woof")


woofy = Dog()
woofy.walk()
woofy.bark()