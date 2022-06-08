countries = {
    'uk' : "manchester",
    'france' : 'paris',
    'germany' : 'berlin',
    'spain' : 'madrid',
    'italy' : 'rome'
}

def add_country(country: str, capital: str):
    countries.setdefault(country, capital)

def dict_inspect(item:dict):
    print('#######################')
    for x in item:
        print(f'|{x :6} > {item[x]:12}|')
    print('#######################')

def define_new_country():
    user_adding = True
    while user_adding:
        user_add_country = input('Please type the name of the contry you wish to add: ')
        user_add_capital = input('Please type the name of the capital for that contry: ')
        add_country(user_add_country, user_add_capital)
        continue_query = input('would you like to add another? Y|N \n')
        match continue_query.capitalize():
            case 'Y' | 'YES': print('returning ...')
            case 'N' | 'NO': user_adding = False
    dict_inspect(countries)

define_new_country()