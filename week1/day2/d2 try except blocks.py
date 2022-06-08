# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
#     except:
#         print("\n ERROR: please input only numerical values. \n")
#     print("**************************** \n")
#     add_up()
# add_up()

#


def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
   
    try:
        if (num1 + num2).isnumeric():
            print(num1 + num2)
    except:
        print("There is an error somewhere!")
    else:  
        print:("This error is getting weird")
    finally:
        print("It's over")
add_up():