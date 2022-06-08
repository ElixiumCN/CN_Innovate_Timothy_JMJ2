print (int(5.4))
print (int("54"))

print (int(round(5.9999)))
print(int("54"))


print (float(54))
print (float("54"))

str1 = str(54)
str2 = str(54)

# converting things from strings to integers to floats

# concatenating strings
print("my pin number is...", (str1 + str2))
variable_one = 0.00001
variable_one = ""

variable_one = True

if variable_one:
    print(f"this is truthy: {variable_one}")
else:
    print("This is falsy")

###########

print("What is your name?")
name = input()

if name:
    print(f"Hello {name}, how are you?")
else:
    print("You did not give me name name!")



list_of_cards = [
    "Jack",
    "Queen",
    "King",
    "Ace",
]

if "Ace" not in list_of_cards:
    print("The Ace is missing")
elif "2" not in list_of_cards and "3" not in list_of_cards:
    print("The list has positive equity")

    if "ten" not in list_of_cards:
        print("Ten is missing")
        list_of_cards.append("Ten")
        for card in list_of_cards:
            print(card)


def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    print(num1 + num2)
#cast these vastiables as integers

add_up()