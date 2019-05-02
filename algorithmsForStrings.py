my_list = ['a', 'a', 'b']

#a set can not hold duplicates
my_set = set(my_list)

print(my_set)

my_list2 = list(sorted(my_set))

print(my_list2)
print(type(my_list2))
given_list2=[1,3,4,1,3]

print(sum(set(given_list2)))


#find the first recurring character
def firstRecurringCharacter(text):
    compare_string = ""
    for letter in text:
        if letter in compare_string:
            return(letter)
        compare_string += letter
    return("No recurring character found")

print(firstRecurringCharacter("abcdefghjjbcaa"))
print(firstRecurringCharacter("bcdefg"))

#find the longest consecutive character
def longestConsecutiveCharacter(input):
    max_count = 0
    max_char = ""
    prev_char = ""
    for letter in input:
        if prev_char == letter:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = letter
        prev_char = letter
    return(max_char,max_count)


print(longestConsecutiveCharacter("aabbcccdddeeeee"))

