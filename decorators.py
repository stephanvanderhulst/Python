def cough_dec(func):

    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('*cough*')

    return func_wrapper

@cough_dec #we can apply this wrapper to any function
def question():
    print('Can you give me money')

@cough_dec
def answer():
    print('NO')


question()
answer()