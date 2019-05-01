#list comprehension
xyz = [i for i in range(5)]
print(xyz)


#generator expression
xyz = (i for i in range(5))
print(xyz) #a generator object that can be iterated over

for i in xyz:
    print(i)


names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    print(f'Hello there {name}')


d = {'Arnold': 18, 'Bernard': 19, 'Ford': 21}
s = "They are {Arnold}, {Bernard}, {Ford} years old"
print(s.format(**d))
x = 42
s2 = "The cake is {}".format("the answer" if x == 42 else 'a lie')
print(s2)
d2 = {'Arnold': 181, 'Bernard': 192, 'Ford': 213}
#This is weird
print(s.format(**d if x == 43 else d2))


#loop over a generator object to find inputs that are divisible by 5
input_list = [5,2,3,1,8,15,20,4,2]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))
#print(xyz)
#for i in xyz:
#    print(i)

#or use:

[print(i) for i in xyz] #one liner for loop


#zip function
x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
    print(a, b, c)

print(zip(x, y, z)) #an object that we can iterate over

for i in(zip(x, y, z)):
    print(i)


combo = (3, 6, 1)

for i in range(10**3):
    if (i%10, int((i/10)%10), int((i/10**2)%10)) == combo:
        print(f'found combo: {i%10, int((i/10)%10), int((i/10**2)%10)}')
        break