# Slicing lists / slicing notation

alphabet = ["a"]

num = input("number")
num = int(num) -1

def choose_a():
    print(alphabet[num])


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

# define a list

for letter in alphabet:
    print(letter)

# create a for loop, it runs the loop from the beginning of the list to the end of the list
# run these commands for each interaction of the loop

number_choice = int(input("Put in a number here and you will be returned the corresponding letter "))-1
print(alphabet[number_choice])

# user input


def get_usernum():
    usernum = input("Please choose a number between 1 and 26!")
    usernum = int(usernum) - 1
    # cast as integer, -1
    print(usernum)


