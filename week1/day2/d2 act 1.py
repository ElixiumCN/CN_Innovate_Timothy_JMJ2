
# number_choice = int(input("Put in a number here and you will be returned the corresponding letter "))-1

#         print("Number successfully entered")
#         print("You didn't input a number, try again")


# examples


def user_choice(): # define function
    choice_check = False # create variable 
    while choice_check == False: # while variable is false, execute following lines
        user_input = input('Please enter a number: \n') # ask the user for input
        if user_input.isnumeric(): # if user input is numeric, continue
            print(f'{user_input} is a number!') # print formatted string
            user_input = int(user_input) # convert the user input to be integer, how is this possible?
            print(type(user_input))  # print formatted string
            choice_check = True # change variable to be true if user entered numeric input
        else: # if user input is not numeric, execute following lines
            print(f'{user_input} is not a number!') # print formatted string
            

user_choice() # execute function without arguments


# try and except to catch errors. e.g. the string "cat" is not an integer

# example

def program():
    user_input = input("Please enter a number!:\n")
    user_input = int(user_input)
    if int(user_input):
        # print (f(int(user_input))
        print (f"{user_input},type{user_input}")
    else:
        print("Try again")
        # print(f"{user_input}",type(user_input))
        program()

program()