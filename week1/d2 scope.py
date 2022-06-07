light = False

def light_switch(): 
    global light
    if light:
        print("Whoa! It’s bright in here") 
        light = False
    else:
        print("Who turned out the lights?")
        light = True

light_switch()


num = 10

def show_num():
    num = 13
    return(num)


def add_num(x):
    x = 15
    print(x)

    add_num(show_num())



def add_num(x):
    x = x % 3
    print(x)

    