#double prize money weekend
prizes = [5,10,15,20,50]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)

print(dbl_prizes)

# now the comprehension method
dbl_prizes = [prize*2 for prize in prizes]

print(dbl_prizes)

# number squaring
nums = [1,2,3,4,5,6,7,8,9,10]

squared_even_nums = []
for num in nums:
    if(num ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)

print(squared_even_nums)

#again lets try the comprehension method
squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]

print(squared_even_nums)

#maps
#jumble the letters in a word
from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot','carrots','potatoes']
anagrams = []

for word in words:
    anagrams.append(jumble(word))
print(anagrams)

#now lets use a map function to do the same
print(list(map(jumble, words)))

#now the comprehension way again
print([jumble(word) for word in words])

#filter method to filter out bad grades
grades = ['A','B','F','C','F','A']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails, grades)))