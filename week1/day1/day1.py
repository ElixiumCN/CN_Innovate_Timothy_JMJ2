from optparse import Values
import random

from numpy import equal, var
import models


new_user = models.User("Senpai", "36", "sen@pai.com")
num1 = random.randint(1, 50)

result = models.add_up(2,2)

greeting = "Hello World"

print(greeting)


print(len(greeting))

print(greeting[1])

print()

# strip white space
# count "a"

example_string = "the quick brown fox"
# print(example_string.strip())

example_string.replace("quick", "fast")

print(example_string)


variable_one = 10

variable_two = "cat"

print(variable_one)

def function_example():
    # do stuff
    pass

# String interpolation


name = "Will"
age = 31
email = "will@will.com"
profession = "Developer/ Instructor"
shoe_size = 10.5
hair_colour = "black"

print "{}, is {} years old, his email is {}, his shoe size is {} and his hair colour is {}".format(name, age, email, professional, shoe_size, hair)

# String interpolation

print("Welcome, {}, are you staying long?".format(name))
# f Strings far better than .format. Don't use .format.
print(f"{name}, is {age} years old, his email is {email}, his shoe size is {shoe_size} and his hair colour is {hair_colour}")

print(email)

# print to trace the value of something
# assigning variable new value .. assignment operator
email = "will.oc@googlemail.com"

num = 10

result = num % 4
# how many times 4 goes into num, what is the remainder?
print(result)

# modulus operator

if num % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")
# Assignment operators to store Values

num2 = 10
# update value
num2 += 2
num2 /= 2

print(num2)

# input using terminal

x = input("What is the first number you would like to add")
y = input("What is the second number you would like to add")

print(type(x))
x = int(x)
x = int(y)
print(add_up(x, y))

# linear running code

music = "Something indeed"
music_list = [
    "Metal"
    "Rock",
    "Samba",
    "Jazz"
]

if "indeed" in music_list or music == "Synthwave":
    print("I'm interested")
elif music == "samba":
    print("Something happens")
elif music != "kpop":
    print("Something else happens")

from models import var

if var:
    print(var)

else:("empty")

# == equal
## != Not equal
# 

# 
# 

def function_one(name):
    return f"hello{name}!"


print(function_one("Brian"))


def multiply(num1, num2):
   return num1 * num2

# print sends to terminal
# return gives value inside program
# return... giving out result of code executed in function
# return keyword is like Equals button on a calculator.
# need return keyword to return value to pass to next 
# line of code.
# return is the final result of a function.

# pass back information from a function

multiply (2, 12)

def multiply(str1, str2):
    return f"{str1}" is my favorite book, and "{str2}" is my favorite film."


print(string_test("The Dark Tower", "Blues Brothers"))

w_amount = 100
account_num = 12345678

def cash_withdrawal(amount, accnum):
    print(f"Withdrawing {amount}" from account {accnum})


list_of_players = [
    "Kane",
    "Son",
    "Emerson"

]

list_of_players[1] = "Jameson"
print(list_of_players)

#zero indexed
print(list_of_players[0])

for i in list_of_players:
    print(i)
    # i i n index
# loop through list
# use anything not just "i"

print(len(list_of_players[2])) # number of characters in third item of list
print(len(list_of_players)) # number of items in list

list_of_players.append("Lloris")
# add item to list
print(list_of_players)

list_of_players.remove()
# remove item with index position
list_of_players.pop(1) 
# remove item with index position
list_of_players.pop
# remove last item on the list

list_of_players.remove(list_of_players[0])
list_of_players.remove(Kane)

list_of_players.remove(list_of_players[0:-1:])

print(list_of_players)
print(first_entry)

# lists: reverse, sort, count, extend

# for loops

for i in range(0, 10, 1):
    print(i)

for x in range(0, 21, 2):
    print(x)
# only the even numbers bcs it goes in steps of 2

for j in range (0, 31, 3):
    print(j)

# while loop.. don't know how many times you want to loop through something... for as long as a condition is met.
# 

num = 0

while num < 10:
    print(num)
    num += 1
    print(num)



from random import randint
num = randint(0,50)
# whilst num isn't 31... generate random integer...
# until randint generates 31
while num != 31:
    num = randint(0, 50)
    print(num)


    


