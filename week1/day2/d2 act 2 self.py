
import random

# def roll_dice_quotes():

# lists
cast_members = [
    "Keanu Reeves",
    "Laurence Fishburne"
    "Gloria Foster"
]

random_quotes = [
    "Oracle Q: What do men with power want? A: More power",
    "Morpheus: That you are a slave, Neo. Like everyone else you were born into bondage. Into a prison that you cannot taste or see or touch. A prison for your mind.",
    "Morpheus: You have to understand, most people are not ready to be unplugged..."
]

# create function
def choose_quote():
    print(random.choice(random_quotes))

# execute function
choose_quote()

# create game

# 

user_input = input('Please enter a number between 1 and 3 \n')

def user_choice():
    if user_input in range(1,3): # if user input is in range
        user_input = int(user_input) # convert the user input to be integer
        (print('test'))     
        # choose_quote()
    else: (print('Try again'))

user_choice()


# user_input = 0
# while not int(shift) in range(1,27):
#     shift = input("Please enter your shift (1 - 26) : ")#choose a shift

# print()


# def user_choice(): # define function
#     choice_check = False # create variable 
#     while choice_check == False: # while variable is false, execute following lines
#         user_input = input('Please enter a number: \n') # ask the user for input
#         if user_input.isnumeric(): # if user input is numeric, continue
#             print(f'{user_input} is a number!') # print formatted string
#             user_input = int(user_input) # convert the user input to be integer, how is this possible?
#             print(type(user_input))  # print formatted string
#             choice_check = True # change variable to be true if user entered numeric input
#         else: # if user input is not numeric, execute following lines
#             print(f'{user_input} is not a number!') # print formatted string
            

# user_choice() # execute function without arguments

# # a while loop trivia game that only stops once you get a question right? G
            

