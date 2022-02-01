# lambda function syntax
# lambda arg1, arg2: expression to return

# example 
lambda num: num ** 2

def square(num):
    return num ** 2 


#This higher-order function has a parameter of a callback function
def a_function(callback):
    print(callback(3))

# This calls the higher-order function with a lambda function argument
a_function(lambda num : num ** 2) # this would print 9 


