def Seattle():
    dogs = 1000
    print('Seattle has', dogs, 'dogs.')

def Bellevue():
    dogs = 2000
    print('Bellevue has', dogs, 'dogs.')

# Program output:

my_string = "Set in global scope"

def main():
    my_string = "Set in local scope"

main()
print(my_string)
# this will print out "Set in global scope"


my_string = "Set in global scope"

def main():
    global my_string
    my_string = "Set in local scope"

main()
print(my_string)
# this will print out "Set in local scope"

