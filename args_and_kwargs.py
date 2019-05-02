blog_1 = "I am so awesome"
blog_2 = "Cars are cool"
blog_3 = "Look at that cat"

def blog_posts(*args):
    for post in args:
        print(post)

blog_posts(blog_1)
blog_posts(blog_1,blog_2,blog_3)