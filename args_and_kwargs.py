blog_1 = "I am so awesome"
blog_2 = "Cars are cool"
blog_3 = "Look at that cat"

def blog_posts(*args):
    for post in args:
        print(post)

blog_posts(blog_1)
blog_posts(blog_1,blog_2,blog_3)


#a kwarg is a keyword argument, for example:
def increment(number, by):
    return number + by

#"by" is the keyword argument, it can make reading code easier
print(increment(2, by=1))


#this is the syntax to pass a variable number of arguments to a function
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number #shorter version of result = result * number
    print(result)


multiply(2, 3, 4, 5)


#now lets pass multiple keyword arguments to a function
def save_user(**user):
    print(user) #prints a dictionary


save_user(id=1, name='John', age=22)