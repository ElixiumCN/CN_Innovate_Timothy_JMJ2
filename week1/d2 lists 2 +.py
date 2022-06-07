for i in range (0,10,1):
    print(i)


my_list = [ 
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

print(my_list[0:5]) # using start and stop
print(my_list[4:])
print(my_list[1:-2])
print(my_list[-2:2])
print(my_list[0:1:2])

def get_usernum():
    usernum = input("Please choose a number between 1 and 26!")
    usernum = int(usernum) - 1     # cast as integer, -1
    print(usernum)
    return alphabet[usernum::(usernum+1)]
    # return alphabet[0:(usernum+1)]


print(get_usernum())

