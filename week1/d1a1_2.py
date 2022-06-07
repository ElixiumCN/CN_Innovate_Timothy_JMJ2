welcome = "Welcome to Code Nation"

def even_length(str):
    str_len = len(str) 
# define variable = str is an argument? that the coder defines when calling the function e.g. even_length(welcome)

    if str_len % 2 == 0:
        print(welcome)
        print("The amount of characters (and spaces) is even")

# If string length is even then print welcome "even"

    else:
        print(welcome)
        print("The amount of characters (and spaces) is not even")

# If string length not even then print welcome "not even"


even_length(welcome)