from math import factorial


name = 'Brain'

def doSomething():
    # name = 'George' 
    # could be called a local scope or functional scope, order: local scope -> Enclosing Scope -> Global Scope 
    print(name)
    # name = 'paul'
    def doSomethingElse():
        print(name)

    doSomethingElse()

doSomething()

# example

name = 'Brain'

def doSomething():
    #Brain has class1, Paul has class1, Serge has class2 
    for name in ['Brain','Paul','Serge']:
        class1 = 'Python'
        print(name)

doSomething()

# example

name = 'Brain'

def doSomething():
    class1 = 'Python' #Now all brain, paul, serge has the same class1 
    for name in ['Brain','Paul','Serge']:
        print(name)

doSomething()

# example recursion 
from cgitb import reset 
from random import randint as taco
import re;

num = taco(3,10)

def add(a,b):
    return a+b

def main():
    result = add(1,1)
    return result

main()

# example recursion 

'''
A function that calls itself 

Similar to Loops

Searching 
Navigating
Sorting
Removing
'''

# num = 5 
# while num > 0:
#     print(num)
#     num -= 1

for i in range(5,0,-1):
    print(i)

def recursion(n):
    if n == 0:
        print(n)
        return
    print(n)
    return recursion(n-1)

recursion(5)

print(factorial(5))

# 5! 5x4x3x2x1 -> 120 

# example 

def recursion(num):
    if n == 0:
        print(n)
        return
    print(n)
    return num*factorial(n-1)

print(factorial(5))

# 1x2x3x4x5 = 130   

def doTheMath(function, a, b):
    return function(a,b)

def add(a,b):
    return a+b

def sub(a,b):
    pass 

# example

places = []
returned = []

def fibonacci(n):
    if n == 0: 
        return 0

    elif n == 1 :
        # returned.append(n)
        # places.append(n)
        return 1
    
    else:
        # places.append(n)
        return fibonacci(n-1) + fibonacci(n-2)

    0,1 # 1
    1,1 # 2S
    1,2 # 3
    2,3 # 5 

print(fibonacci)





