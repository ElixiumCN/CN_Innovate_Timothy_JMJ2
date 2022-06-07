from random import randint as r

ghost_chars = [
    'Peter Venkman', 'Raymond Stantz', 'Egon Spengler',
    'Winston Zeddemore', 'Dana Barrett', 'Lenny Clotch',
    'Janine Melnitz', 'Louis Tully', 'Walter Peck',
    'Joanne Phillips', 'Sammy Kipper', 'George Washington',
    'Frank Joslin', 'Meryl Campbell', 'Jhon Plisken',
    'John Conner', 'Kyle Reece', 'Sarah Connor'
]

def ghost_game(char_list): # create function
    p_lives = 3 # create player lives variable with value 3
    print('You have 3 lives, would you like to begin? Press enter to continue')
    input() # not sure
    while p_lives > 0: # While player lives is above zero, run code
        question = r(0, 17) # set the question var to be a random int between 0 and 17 
# there should be a list of questions somewhere?

        pressed_question = char_list[question]
        print(f'is {pressed_question} in the Ghostbusters film? [Y/N]\n')
        user_answer = input()
        if question >= 9:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is indeed a charater in the movie!')
                case 'N' | "NO":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives = (p_lives -1)
        else:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives = (p_lives -1)
                case 'N' | "NO":
                    print(f'{pressed_question} is indeed a charater in the movie!')
    print('You have run out of lives! GAME OVER!!!!')

ghost_game(ghost_chars)