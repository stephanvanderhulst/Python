#lambda functions
nums = [1,2,3,4,5,6]

def square(n):
    return n * n

print(list(map(square, nums)))

#now lets use an inline anomymous lambda function, good when we are only going to use a function once
print(list(map(lambda n: n * n, nums)))