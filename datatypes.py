#the primitive datatypes for python:
#integers
#float
#strings
#boolean
print(8/5)


#dictionaries

ninja_belts = {"crystal": "red", "ryu": "black"}

def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_intro(ninja_belts)


#sort the list
[1,6,3,9,8,5]