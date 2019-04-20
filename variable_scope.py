#variable scope
my_name = "ryu"

#overriding the variable locally
def print_name():
#    global my_name #this will override it globally
    my_name = "yoshi"
    print('the name inside the function is', my_name)

print_name()
print('the name outside the function is', my_name)